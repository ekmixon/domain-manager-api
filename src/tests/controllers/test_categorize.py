"""Categorize domain controller tests."""
# Standard Python Libraries
from unittest import mock

# Third-Party Libraries
from api.controllers.categorization import categorization_manager
from api.documents.active_site import ActiveSite
from faker import Faker

faker = Faker()


@mock.patch.object(ActiveSite, "get_by_id")
def test_categorize_domain(mock_get, app):
    """Test categorize a domain."""
    live_site_id = faker.pyint()

    domain = categorization_manager(live_site_id=live_site_id)

    assert mock.call(domain, mock_get.call_args_list)