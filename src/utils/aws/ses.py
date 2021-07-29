"""Create DNS email records from SES."""
# Third-Party Libraries
import boto3

route53 = boto3.client("route53")
ses = boto3.client("ses")


def list_hosted_zones(names_only: bool = False):
    """
    List hosted zones.

    Set names_only to true if only hosted zone names are needed.
    """
    if not names_only:
        return route53.list_hosted_zones()["HostedZones"]

    return [hosted_zone.get("Name") for hosted_zone in list_hosted_zones()]


def get_dns_id(domain_name: str):
    """Get hosted zone ID."""
    if f"{domain_name}." not in list_hosted_zones(names_only=True):
        return "Domain's hosted zone does not exist."

    return "".join(
        hosted_zone.get("Id")
        for hosted_zone in list_hosted_zones()
        if hosted_zone.get("Name") == f"{domain_name}."
    )


def enable_email_receiving(domain_name: str):
    """Enable receiving emails for a specified domain."""
    dns_id = get_dns_id(domain_name=domain_name)

    # Generate verification token
    verification_token = ses.verify_domain_identity(Domain=domain_name)[
        "VerificationToken"
    ]

    # Generate CNAME record DKIM tokens
    dkim_token_1, dkim_token_2, dkim_token_3 = ses.verify_domain_dkim(
        Domain=domain_name
    )["DkimTokens"]

    response = route53.change_resource_record_sets(
        HostedZoneId=dns_id,
        ChangeBatch={
            "Comment": "",
            "Changes": [
                {
                    "Action": "UPSERT",
                    "ResourceRecordSet": {
                        "Name": f"_amazonses.{domain_name}",
                        "Type": "TXT",
                        "TTL": 300,
                        "ResourceRecords": [{"Value": f'"{verification_token}"'}],
                    },
                },
                {
                    "Action": "UPSERT",
                    "ResourceRecordSet": {
                        "Name": f"{dkim_token_1}._domainkey.{domain_name}",
                        "Type": "CNAME",
                        "TTL": 300,
                        "ResourceRecords": [{"Value": f"{dkim_token_1}.amazonses.com"}],
                    },
                },
                {
                    "Action": "UPSERT",
                    "ResourceRecordSet": {
                        "Name": f"{dkim_token_2}._domainkey.{domain_name}",
                        "Type": "CNAME",
                        "TTL": 300,
                        "ResourceRecords": [{"Value": f"{dkim_token_2}.amazonses.com"}],
                    },
                },
                {
                    "Action": "UPSERT",
                    "ResourceRecordSet": {
                        "Name": f"{dkim_token_3}._domainkey.{domain_name}",
                        "Type": "CNAME",
                        "TTL": 300,
                        "ResourceRecords": [{"Value": f"{dkim_token_3}.amazonses.com"}],
                    },
                },
            ],
        },
    )

    return response


def disable_email_receiving(domain_name: str):
    """Disable receiving emails for a specified domain."""
    get_dns_id(domain_name=domain_name)
    return ses.delete_identity(Identity=domain_name)
