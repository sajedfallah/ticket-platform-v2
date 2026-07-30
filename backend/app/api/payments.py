from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.payments.provider import PaymentRequest, PaymentStatus, payment_provider
from app.services.fulfillment_service import fulfillment_service
from app.services.mvp_flow_service import mvp_flow_service

router = APIRouter(prefix="/payments", tags=["payments"])


class CreatePaymentPayload(BaseModel):
    order_id: int = Field(gt=0)
    callback_url: str = Field(min_length=8)


class VerifyPaymentPayload(BaseModel):
    payment_id: str = Field(min_length=8)
    success: bool


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_payment(payload: CreatePaymentPayload):
    order = mvp_flow_service.get_order(payload.order_id)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="order_not_found")
    if order.status not in {"pending", "payment_failed"}:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="order_not_payable",
        )

    session = payment_provider.create_payment(
        PaymentRequest(
            order_id=order.id,
            amount=order.total_amount,
            callback_url=payload.callback_url,
            currency=order.currency,
        )
    )
    updated_order = mvp_flow_service.attach_payment(order.id, session.payment_id)
    return {
        "payment_id": session.payment_id,
        "order_id": session.order_id,
        "amount": updated_order.total_amount,
        "currency": updated_order.currency,
        "status": session.status.value,
        "redirect_url": session.redirect_url,
        "order": mvp_flow_service.serialize(updated_order),
    }


@router.post("/verify")
def verify_payment(payload: VerifyPaymentPayload):
    try:
        result = payment_provider.verify_payment(payload.payment_id, payload.success)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc

    order = mvp_flow_service.get_order(result.order_id)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="order_not_found")
    if order.payment_id != result.payment_id:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="payment_order_mismatch")

    ticket = None
    if result.status is PaymentStatus.PAID:
        updated_order = mvp_flow_service.mark_paid(result.order_id, result.payment_id)
        ticket = fulfillment_service.fulfill_paid_order(
            order_id=result.order_id,
            payment_id=result.payment_id,
            transaction_id=result.transaction_id or "",
        )
    else:
        updated_order = mvp_flow_service.mark_payment_failed(result.order_id, result.payment_id)

    return {
        "payment_id": result.payment_id,
        "order_id": result.order_id,
        "status": result.status.value,
        "transaction_id": result.transaction_id,
        "order": mvp_flow_service.serialize(updated_order),
        "ticket": fulfillment_service.serialize(ticket) if ticket else None,
    }
