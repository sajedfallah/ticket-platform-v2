from pydantic import BaseModel
from typing import Optional

class EventBase(BaseModel):
    title: str
    description: Optional[str] = None
    category: Optional[str] = None

class EventCreate(EventBase):
    pass

class EventResponse(EventBase):
    id: int

    class Config:
        from_attributes = True
