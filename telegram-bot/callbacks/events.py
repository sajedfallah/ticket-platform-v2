"""Event callback handlers."""


def handle_event_selection(event_id: int):
    return {"action": "select_event", "event_id": event_id}
