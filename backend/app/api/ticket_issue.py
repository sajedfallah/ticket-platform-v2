from fastapi import APIRouter, HTTPException, status

from app.services.fulfillment_service import fulfillment_service
from app.services.qr_service import generate_ticket_code

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.post("/issue", status_code=status.HTTP_201_CREATED)
def issue_ticket(payload: dict):
    code = generate_ticket_code()
    return {
        "ticket_code": code,
        "status": "active",
        "payload": payload,
    }


@router.get("/order/{order_id}")
def get_ticket_by_order(order_id: int):
    ticket = fulfillment_service.get_ticket_for_order(order_id)
    if ticket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No issued ticket exists for this order",
        )
    return fulfillment_service.serialize(ticket)


@router.post("/check")
def check_ticket(payload: dict):
    return {"valid": True, "ticket": payload}
