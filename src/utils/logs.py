"""Logging utils."""
# cisagov Libraries
from api.manager import LogManager

log_manager = LogManager()


def cleanup_logs(username):
    """Cleanup log collection."""
    to_keep = log_manager.all(
        params={"username": username},
        sortby={"created": "DESC"},
        limit=100,  # Only keeping 100 for now. Change when a new number is determined.
        fields=["_id"],
    )
    ids = [x.get("_id") for x in to_keep]
    return log_manager.delete(params={"_id": {"$nin": ids}})
