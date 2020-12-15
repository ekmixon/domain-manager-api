"""Categorize domain controller tests."""
# Standard Python Libraries
from unittest import mock

# Third-Party Libraries
from faker import Faker

# cisagov Libraries
from api.controllers.categorization import categorization_manager
from models.website import Website

faker = Faker()


@mock.patch.object(Website, "get")
def test_categorize_domain(mock_get, app):
    """Test categorize a domain."""
    website_id = faker.pyint()

    category = "Health"

    domain = categorization_manager(website_id=website_id, category=category)

    assert mock.call(domain, mock_get.call_args_list)
