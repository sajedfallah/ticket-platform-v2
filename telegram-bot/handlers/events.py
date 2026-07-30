"""Event browsing handler foundation."""


def events_message(events=None):
    if not events:
        return "🎵 No events available"
    return "\n".join([f"🎵 {event.get('title', 'Event')}" for event in events])
