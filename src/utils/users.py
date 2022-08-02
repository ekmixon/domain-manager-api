"""User utils."""
# Third-Party Libraries
from flask import g

# cisagov Libraries
from api.config import logger
from api.manager import LogManager, UserManager

user_manager = UserManager()
log_manager = LogManager()


def get_user_groups():
    """Get the groups a user belongs to."""
    try:
        user = user_manager.get(filter_data={"Username": g.username})
        return user["Groups"] if "Groups" in user else []
    except Exception as e:
        logger.exception(e)
        return []


def get_users_group_ids():
    """Get applications a user belongs to."""
    try:
        groups = get_user_groups()
        return [group["Application_Id"] for group in groups]

    except Exception as e:
        logger.exception(e)
        return []


def user_can_access_domain(domain):
    """Check whether user can access domain."""
    try:
        if g.is_admin:
            return True
        groups = get_users_group_ids()
        return "application_id" in domain and domain["application_id"] in groups
    except Exception as e:
        logger.exception(e)
        return False


def get_email_from_user(user):
    """Get email address for user returned by cognito or database."""
    key = "UserAttributes" if "UserAttributes" in user else "Attributes"
    return next(filter(lambda x: x["Name"] == "email", user[key]), {}).get("Value")


def get_emails_from_users(users):
    """Get emails from a list of users from cognito or database."""
    emails = []
    for user in users:
        email = user["Email"] if user.get("Email") else get_email_from_user(user)
        if email:
            emails.append(email)
    return emails


def get_users_in_group(application_id: str, return_emails: bool = False):
    """Get all users in group."""
    users = user_manager.all(params={"Groups.Application_Id": application_id})
    return get_emails_from_users(users) if return_emails else users
