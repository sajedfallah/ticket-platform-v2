from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.services.mvp_flow_service import mvp_flow_service

router = APIRouter(prefix="/events", tags=["events"])


class CreateEventPayload(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    description: str = Field(default="", max_length=2000)
    category: str = Field(default="general", min_length=2, max_length=50)
    ticket_name: str = Field(default="General Admission", min_length=2, max_length=100)
    ticket_price: int = Field(gt=0, description="Minor currency units, for example cents")
    currency: str = Field(default="EUR", min_length=3, max_length=3)
    capacity: int = Field(gt=0)
    status: str = Field(default="published", pattern="^(draft|published)$")


@router.get("")
def list_events():
    items = [mvp_flow_service.serialize(event) for event in mvp_flow_service.list_events()]
    return {"items": items, "count": len(items)}


@router.get("/{event_id}")
def get_event(event_id: int):
    event = mvp_flow_service.get_event(event_id)
    if event is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="event_not_found")
    return mvp_flow_service.serialize(event)


@router.post("", status_code=status.HTTP_201_CREATED)
def create_event(payload: CreateEventPayload):
    event = mvp_flow_service.create_event(**payload.model_dump())
    return mvp_flow_service.serialize(event)
