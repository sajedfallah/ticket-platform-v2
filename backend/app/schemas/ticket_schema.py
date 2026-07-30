from pydantic import BaseModel
from typing import Optional

class TicketCreate(BaseModel):
    order_id: int

class TicketResponse(BaseModel):
    id: int
    ticket_code: str
    status: Optional[str] = None

    class Config:
        from_attributes = True
