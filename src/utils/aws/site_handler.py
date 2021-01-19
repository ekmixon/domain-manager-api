"""AWS site gneeration utilities."""
# Standard Python Libraries
from datetime import datetime
import time

# Third-Party Libraries
import boto3
import dns.resolver

# cisagov Libraries
from settings import WEBSITE_BUCKET_URL, logger

# Initialize aws clients
acm = boto3.client("acm")
cloudfront = boto3.client("cloudfront")
route53 = boto3.client("route53")


def launch_site(website):
    """Launch an active site onto s3."""
    # Verify that site is owned.
    ns_records = get_hosted_zone_ns_records(website["route53"]["id"])
    verify_hosted_zone(website["name"], ns_records)

    # generate ssl certs and return certificate ARN
    certificate_arn = generate_ssl_certs(website=website)

    # setup cloudfront
    distribution_id, distribution_endpoint = setup_cloudfront(
        website=website, certificate_arn=certificate_arn
    )

    # setup DNS
    setup_dns(website=website, endpoint=distribution_endpoint)

    return {
        "cloudfront": {
            "id": distribution_id,
            "distribution_endpoint": distribution_endpoint,
        },
        "acm": {"certificate_arn": certificate_arn},
    }


def delete_site(website):
    """Delete an active site off s3."""
    cloudfront_metadata = website["cloudfront"]

    # get distribution config
    distribution = cloudfront.get_distribution(Id=cloudfront_metadata["id"])

    # disable cloudfront distribution
    distribution["Distribution"]["DistributionConfig"]["Enabled"] = False
    cloudfront.update_distribution(
        Id=cloudfront_metadata["id"],
        IfMatch=distribution["ETag"],
        DistributionConfig=distribution["Distribution"]["DistributionConfig"],
    )

    # wait until distribution is fully disabled
    while True:
        time.sleep(2)
        status = cloudfront.get_distribution(Id=cloudfront_metadata["id"])
        if (
            status["Distribution"]["DistributionConfig"]["Enabled"] is False
            and status["Distribution"]["Status"] == "Deployed"
        ):
            break

    # delete cloudfront distribution
    cloudfront.delete_distribution(Id=cloudfront_metadata["id"], IfMatch=status["ETag"])

    # delete acm ssl certificates
    acm.delete_certificate(CertificateArn=website["acm"]["certificate_arn"])
    delete_ssl_certs(website)

    response = delete_dns(
        website=website, endpoint=cloudfront_metadata["distribution_endpoint"]
    )
    return response


def setup_cloudfront(website, certificate_arn):
    """Create AWS CloudFront Distribution."""
    # Launch CloudFront distribution
    unique_identifier = datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
    domain_name = website["name"]

    distribution_config = {
        "CallerReference": unique_identifier,
        "Aliases": {"Quantity": 1, "Items": [domain_name]},
        "DefaultRootObject": "home.html",
        "Comment": "Managed by Domain Manager",
        "Enabled": True,
        "Origins": {
            "Quantity": 1,
            "Items": [
                {
                    "Id": "1",
                    "DomainName": WEBSITE_BUCKET_URL,
                    "OriginPath": f"/{domain_name}",
                    "CustomOriginConfig": {
                        "HTTPPort": 80,
                        "HTTPSPort": 443,
                        "OriginProtocolPolicy": "http-only",
                    },
                }
            ],
        },
        "DefaultCacheBehavior": {
            "TargetOriginId": "1",
            "ViewerProtocolPolicy": "redirect-to-https",
            "TrustedSigners": {"Quantity": 0, "Enabled": False},
            "ForwardedValues": {
                "QueryString": False,
                "Cookies": {"Forward": "all"},
                "Headers": {"Quantity": 0},
                "QueryStringCacheKeys": {"Quantity": 0},
            },
            "MinTTL": 1000,
        },
        "ViewerCertificate": {
            "ACMCertificateArn": certificate_arn,
            "SSLSupportMethod": "sni-only",
            "MinimumProtocolVersion": "TLSv1.2_2019",
        },
    }

    distribution = cloudfront.create_distribution(
        DistributionConfig=distribution_config
    )

    return (
        distribution["Distribution"]["Id"],
        distribution["Distribution"]["DomainName"],
    )


def setup_dns(website, endpoint=None, ip_address=None):
    """Create a domain's DNS."""
    domain_name = website["name"]
    dns_id = website["route53"]["id"]
    if ip_address:
        response = route53.change_resource_record_sets(
            HostedZoneId=dns_id,
            ChangeBatch={
                "Comment": ip_address,
                "Changes": [
                    {
                        "Action": "UPSERT",
                        "ResourceRecordSet": {
                            "Name": domain_name,
                            "Type": "A",
                            "TTL": 15,
                            "ResourceRecords": [{"Value": ip_address}],
                        },
                    }
                ],
            },
        )
    else:
        response = route53.change_resource_record_sets(
            HostedZoneId=dns_id,
            ChangeBatch={
                "Comment": domain_name,
                "Changes": [
                    {
                        "Action": "UPSERT",
                        "ResourceRecordSet": {
                            "Name": domain_name,
                            "Type": "A",
                            "AliasTarget": {
                                "HostedZoneId": "Z2FDTNDATAQYW2",
                                "EvaluateTargetHealth": False,
                                "DNSName": endpoint,
                            },
                        },
                    }
                ],
            },
        )
    logger.info(response)
    return response


def delete_dns(website, endpoint=None, ip_address=None):
    """Create a domain's DNS."""
    domain_name = website["name"]
    dns_id = website["route53"]["id"]
    if ip_address:
        response = route53.change_resource_record_sets(
            HostedZoneId=dns_id,
            ChangeBatch={
                "Comment": ip_address,
                "Changes": [
                    {
                        "Action": "DELETE",
                        "ResourceRecordSet": {
                            "Name": domain_name,
                            "Type": "A",
                            "TTL": 15,
                            "ResourceRecords": [{"Value": ip_address}],
                        },
                    }
                ],
            },
        )
    else:
        response = route53.change_resource_record_sets(
            HostedZoneId=dns_id,
            ChangeBatch={
                "Comment": domain_name,
                "Changes": [
                    {
                        "Action": "DELETE",
                        "ResourceRecordSet": {
                            "Name": domain_name,
                            "Type": "A",
                            "AliasTarget": {
                                "HostedZoneId": "Z2FDTNDATAQYW2",
                                "EvaluateTargetHealth": False,
                                "DNSName": endpoint,
                            },
                        },
                    }
                ],
            },
        )
    logger.info(response)
    return response


def generate_ssl_certs(website):
    """Request and Validate an SSL certificate using AWS Certificate Manager."""
    domain_name = website["name"]
    dns_id = website["route53"]["id"]
    requested_certificate = acm.request_certificate(
        DomainName=domain_name,
        ValidationMethod="DNS",
        SubjectAlternativeNames=[domain_name],
        DomainValidationOptions=[
            {"DomainName": domain_name, "ValidationDomain": domain_name},
        ],
        Options={"CertificateTransparencyLoggingPreference": "ENABLED"},
    )

    cert_arn = requested_certificate["CertificateArn"]
    acm_record = None
    while not acm_record:
        time.sleep(2)
        acm_record = get_acm_record(cert_arn)

    # add validation record to the dns
    route53.change_resource_record_sets(
        HostedZoneId=dns_id,
        ChangeBatch={
            "Comment": domain_name,
            "Changes": [
                {
                    "Action": "UPSERT",
                    "ResourceRecordSet": {
                        "Name": acm_record["Name"],
                        "Type": "CNAME",
                        "TTL": 30,
                        "ResourceRecords": [{"Value": acm_record["Value"]}],
                    },
                }
            ],
        },
    )

    # wait until the certificate has been validated
    waiter = acm.get_waiter("certificate_validated")
    waiter.wait(CertificateArn=cert_arn)

    return cert_arn


def delete_ssl_certs(website):
    """Delete acm ssl certs."""
    cert_arn = website["acm"]["certificate_arn"]
    acm_record = get_acm_record(cert_arn)
    route53.change_resource_record_sets(
        HostedZoneId=website["route53"]["id"],
        ChangeBatch={
            "Changes": [
                {
                    "Action": "DELETE",
                    "ResourceRecordSet": {
                        "Name": acm_record["Name"],
                        "Type": "CNAME",
                        "TTL": 30,
                        "ResourceRecords": [{"Value": acm_record["Value"]}],
                    },
                }
            ]
        },
    )
    acm.delete_certificate(CertificateArn=cert_arn)


def get_acm_record(cert_arn):
    """Get acm route 53 record for validation."""
    certificate_description = acm.describe_certificate(CertificateArn=cert_arn)
    resource_records = [
        description.get("ResourceRecord", None)
        for description in certificate_description.get("Certificate", {}).get(
            "DomainValidationOptions"
        )
    ][0]
    return resource_records


def get_hosted_zone_ns_records(hosted_zone_id):
    """Get hosted zone NS records."""
    resp = route53.get_hosted_zone(Id=hosted_zone_id)
    return resp["DelegationSet"]["NameServers"]


def verify_hosted_zone(domain_name, r53_nameservers):
    """Verify that we have control of hosted zone."""
    new_nameservers = []
    for server in r53_nameservers:
        if not server.endswith("."):
            server = f"{server}."
        new_nameservers.append(server)

    dns_resolver = dns.resolver.Resolver()
    try:
        response = dns_resolver.resolve(domain_name, "NS").response
    except Exception as e:
        logger.exception(e)
        raise e
    ns_servers = []
    for answer in response.answer[0]:
        ns_servers.append(answer.to_text())
    if len(set(ns_servers) - set(new_nameservers)) > 0:
        raise Exception("Route53 nameservers don't match.")
