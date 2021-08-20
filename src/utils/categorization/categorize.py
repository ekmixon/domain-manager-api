"""Categorization utils."""
# cisagov Libraries
from api.manager import CategorizationManager, DomainManager
from api.schemas.categorization_schema import CategorizationSchema
from utils.categorization import PROXIES
from utils.validator import validate_data

categorization_manager = CategorizationManager()
domain_manager = DomainManager()


def get_domain_proxies(domain_id: str):
    """Get all proxies for a domain."""
    domain_proxies = categorization_manager.all(params={"domain_id": domain_id})
    if not domain_proxies:
        return {"error": "categorization requests for this domain do not exist."}, 400

    return domain_proxies, 200


def post_categorize_request(domain_id: str, requested_category: str):
    """Categorize a domain across proxies."""
    if categorization_manager.get(filter_data={"domain_id": domain_id}):
        return {"error": "categorization requests already exist for this domain."}, 400

    categories_data = [
        {
            "domain_id": domain_id,
            "proxy": proxy["name"],
            "status": "new",
            "category": requested_category,
            "categorize_url": proxy["categorize_url"],
            "check_url": proxy["check_url"],
        }
        for proxy in PROXIES
    ]
    post_data = validate_data(categories_data, CategorizationSchema, many=True)
    categorization_manager.save_many(post_data)

    return {"success": "categorization request has been submitted"}, 200


def put_proxy_status(domain_id: str, proxy_name: str, status: str):
    """Update proxy status for a domain."""
    proxy = categorization_manager.get(
        filter_data={"domain_id": domain_id, "proxy": proxy_name}, fields=["_id"]
    )
    categorization_manager.update(document_id=proxy["_id"], data={"status": status})

    return {"success": "proxy status has been updated"}, 200
