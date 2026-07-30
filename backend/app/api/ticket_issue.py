from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.services.fulfillment_service import fulfillment_service
from app.services.qr_service import generate_ticket_code

router = APIRouter(prefix="/tickets", tags=["tickets"])


class TicketCodePayload(BaseModel):
    ticket_code: str = Field(min_length=6)


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


@router.post("/validate")
def validate_ticket(payload: TicketCodePayload):
    ticket = fulfillment_service.get_ticket_by_code(payload.ticket_code)
    if ticket is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket not found",
        )

    return {
        "valid": ticket.status == "active",
        "ticket": fulfillment_service.serialize(ticket),
    }


@router.post("/check-in")
def check_in_ticket(payload: TicketCodePayload):
    try:
        ticket = fulfillment_service.check_in(payload.ticket_code)
    except LookupError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except RuntimeError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc

    return {
        "valid": True,
        "entry_allowed": True,
        "ticket": fulfillment_service.serialize(ticket),
    }


@router.post("/check")
def check_ticket(payload: TicketCodePayload):
    return validate_ticket(payload)
