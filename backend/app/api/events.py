from fastapi import APIRouter

router = APIRouter(prefix="/api/events", tags=["Events"])


@router.get("")
def list_events():
    return {
        "items": [],
        "message": "Events API ready"
    }


@router.get("/{event_id}")
def get_event(event_id: int):
    return {
        "id": event_id,
        "message": "Event detail endpoint ready"
    }
