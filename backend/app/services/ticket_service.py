import uuid


class TicketService:
    """Ticket generation and validation logic."""

    def generate_ticket_code(self) -> str:
        return f"TKT-{uuid.uuid4().hex[:8].upper()}"

    def validate_ticket(self, ticket_code: str) -> dict:
        return {
            "ticket": ticket_code,
            "valid": True
        }
