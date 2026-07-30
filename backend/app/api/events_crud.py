from fastapi import APIRouter

router = APIRouter(prefix="/events", tags=["events"])

@router.get("")
def list_events():
    return {"items": [], "count": 0}

@router.get("/{event_id}")
def get_event(event_id: int):
    return {"id": event_id, "status": "not_implemented"}

@router.post("")
def create_event(payload: dict):
    return {"created": True, "event": payload}
