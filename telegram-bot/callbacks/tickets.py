"""Ticket selection callback handlers."""


def handle_ticket_selection(ticket_type_id: int):
    return {"action": "select_ticket", "ticket_type_id": ticket_type_id}
