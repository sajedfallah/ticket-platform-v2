"""Ticket handlers for Telegram Bot v2."""

from api_client import TicketAPIClient


async def my_tickets(user_id: int):
    """Fetch and prepare user tickets from backend."""
    client = TicketAPIClient()
    return await client.get_user_tickets(user_id)


async def show_ticket(ticket: dict):
    """Format ticket information for Telegram response."""
    return {
        "title": "Your Ticket",
        "code": ticket.get("ticket_code"),
        "status": ticket.get("status", "active"),
        "qr": ticket.get("qr_code")
    }
