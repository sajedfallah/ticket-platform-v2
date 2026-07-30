from datetime import datetime


def health_status():
    return {
        "status": "ok",
        "service": "ticket-platform-backend",
        "timestamp": datetime.utcnow().isoformat(),
        "database": "pending-check",
        "redis": "pending-check"
    }
