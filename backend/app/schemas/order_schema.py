from pydantic import BaseModel
from typing import Optional

class OrderCreate(BaseModel):
    user_id: int
    event_id: int
    ticket_type_id: int
    quantity: int = 1

class OrderResponse(BaseModel):
    id: int
    order_number: Optional[str] = None
    status: str

    class Config:
        from_attributes = True
