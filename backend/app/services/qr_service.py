import uuid


def generate_ticket_code() -> str:
    return f"TKT-{uuid.uuid4().hex[:8].upper()}"


def generate_qr_payload(ticket_code: str) -> dict:
    return {
        "ticket_code": ticket_code,
        "status": "active"
    }


def validate_qr(ticket_code: str) -> bool:
    return bool(ticket_code)
