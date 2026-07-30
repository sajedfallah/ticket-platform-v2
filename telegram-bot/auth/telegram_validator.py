"""Telegram WebApp validation placeholder.

Production implementation will validate initData signature
before creating authenticated sessions.
"""


def validate_telegram_data(init_data: str) -> bool:
    return bool(init_data)
