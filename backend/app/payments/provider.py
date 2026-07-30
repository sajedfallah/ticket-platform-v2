from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from uuid import uuid4


class PaymentStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"


@dataclass(frozen=True)
class PaymentRequest:
    order_id: int
    amount: int
    callback_url: str
    currency: str = "EUR"


@dataclass(frozen=True)
class PaymentSession:
    payment_id: str
    order_id: int
    status: PaymentStatus
    redirect_url: str


@dataclass(frozen=True)
class PaymentVerification:
    payment_id: str
    order_id: int
    status: PaymentStatus
    transaction_id: str | None = None


class PaymentProvider(ABC):
    @abstractmethod
    def create_payment(self, request: PaymentRequest) -> PaymentSession:
        raise NotImplementedError

    @abstractmethod
    def verify_payment(self, payment_id: str, success: bool) -> PaymentVerification:
        raise NotImplementedError


class MockPaymentProvider(PaymentProvider):
    """Development provider that preserves the production gateway contract."""

    def __init__(self) -> None:
        self._payments: dict[str, PaymentRequest] = {}

    def create_payment(self, request: PaymentRequest) -> PaymentSession:
        payment_id = f"pay_{uuid4().hex}"
        self._payments[payment_id] = request
        return PaymentSession(
            payment_id=payment_id,
            order_id=request.order_id,
            status=PaymentStatus.PENDING,
            redirect_url=f"{request.callback_url}?payment_id={payment_id}",
        )

    def verify_payment(self, payment_id: str, success: bool) -> PaymentVerification:
        request = self._payments.get(payment_id)
        if request is None:
            raise ValueError("payment_not_found")

        status = PaymentStatus.PAID if success else PaymentStatus.FAILED
        transaction_id = f"txn_{uuid4().hex}" if success else None
        return PaymentVerification(
            payment_id=payment_id,
            order_id=request.order_id,
            status=status,
            transaction_id=transaction_id,
        )


payment_provider: PaymentProvider = MockPaymentProvider()
