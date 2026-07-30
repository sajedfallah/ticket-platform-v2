"""User profile handler foundation."""

async def profile(user):
    return {
        "name": user.get("first_name", "User"),
        "username": user.get("username"),
    }
