"""Development seed data for MVP testing."""

EVENTS = [
    {
        "title": "Nexus Music Night",
        "category": "music",
        "status": "published",
    },
    {
        "title": "Summer Festival",
        "category": "festival",
        "status": "published",
    },
]

TICKET_TYPES = [
    {"name": "VIP", "price": 1000000, "capacity": 50},
    {"name": "Gold", "price": 600000, "capacity": 200},
    {"name": "Normal", "price": 300000, "capacity": 500},
]
