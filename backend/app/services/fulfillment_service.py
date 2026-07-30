from dataclasses import asdict, dataclass
from threading import Lock

from app.services.qr_service import generate_ticket_code


@dataclass(frozen=True)
class IssuedTicket:
    ticket_code: str
    order_id: int
    payment_id: str
    transaction_id: str
    status: str = "active"


class FulfillmentService:
    """Issues exactly one ticket for each paid order in the MVP runtime."""

    def __init__(self) -> None:
        self._tickets_by_order: dict[int, IssuedTicket] = {}
        self._lock = Lock()

    def fulfill_paid_order(
        self,
        *,
        order_id: int,
        payment_id: str,
        transaction_id: str,
    ) -> IssuedTicket:
        if order_id <= 0:
            raise ValueError("order_id must be positive")
        if not transaction_id:
            raise ValueError("transaction_id is required")

        with self._lock:
            existing = self._tickets_by_order.get(order_id)
            if existing is not None:
                return existing

            ticket = IssuedTicket(
                ticket_code=generate_ticket_code(),
                order_id=order_id,
                payment_id=payment_id,
                transaction_id=transaction_id,
            )
            self._tickets_by_order[order_id] = ticket
            return ticket

    def get_ticket_for_order(self, order_id: int) -> IssuedTicket | None:
        return self._tickets_by_order.get(order_id)

    @staticmethod
    def serialize(ticket: IssuedTicket) -> dict:
        return asdict(ticket)


fulfillment_service = FulfillmentService()
