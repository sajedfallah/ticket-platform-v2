"""Event selection keyboard helpers."""


def event_buttons(events):
    return [[event.get("title", "Event")] for event in events]
