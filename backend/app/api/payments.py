from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.payments.provider import PaymentRequest, PaymentStatus, payment_provider

router = APIRouter(prefix="/payments", tags=["payments"])


class CreatePaymentPayload(BaseModel):
    order_id: int = Field(gt=0)
    amount: int = Field(gt=0)
    callback_url: str = Field(min_length=8)
    currency: str = Field(default="EUR", min_length=3, max_length=3)


class VerifyPaymentPayload(BaseModel):
    payment_id: str = Field(min_length=8)
    success: bool


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_payment(payload: CreatePaymentPayload):
    session = payment_provider.create_payment(
        PaymentRequest(
            order_id=payload.order_id,
            amount=payload.amount,
            callback_url=payload.callback_url,
            currency=payload.currency.upper(),
        )
    )
    return {
        "payment_id": session.payment_id,
        "order_id": session.order_id,
        "status": session.status.value,
        "redirect_url": session.redirect_url,
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

    return {
        "payment_id": result.payment_id,
        "order_id": result.order_id,
        "status": result.status.value,
        "transaction_id": result.transaction_id,
        "should_issue_ticket": result.status is PaymentStatus.PAID,
    }
