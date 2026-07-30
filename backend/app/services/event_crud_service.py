from sqlalchemy.orm import Session


def create_event(db: Session, event_data):
    """Create event business flow placeholder.

    Database insert logic will be connected after model relationships
    and migration validation are completed.
    """
    return event_data


def list_events(db: Session):
    return []
