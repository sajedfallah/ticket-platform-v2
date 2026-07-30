from enum import Enum


class PaymentStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"


def create_payment(amount: float):
    return {
        "amount": amount,
        "status": PaymentStatus.PENDING.value
    }
