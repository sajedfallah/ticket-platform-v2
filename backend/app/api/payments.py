from fastapi import APIRouter
from app.schemas.payment_schema import PaymentCreate

router = APIRouter(prefix="/api/payments", tags=["payments"])

@router.post("/")
def create_payment(payload: PaymentCreate):
    return {
        "status": "pending",
        "order_id": payload.order_id,
        "amount": payload.amount
    }

@router.get("/{payment_id}")
def get_payment(payment_id: int):
    return {
        "id": payment_id,
        "status": "pending"
    }
