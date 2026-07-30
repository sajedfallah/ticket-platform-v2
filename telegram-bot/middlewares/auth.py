from typing import Optional


def get_telegram_user_id(update) -> Optional[int]:
    """Extract telegram user id from update object."""
    if update.effective_user:
        return update.effective_user.id
    return None
