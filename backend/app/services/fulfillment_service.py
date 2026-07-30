from dataclasses import asdict, dataclass, replace
from datetime import datetime, timezone
from threading import Lock

from app.services.qr_service import generate_ticket_code


@dataclass(frozen=True)
class IssuedTicket:
    ticket_code: str
    order_id: int
    payment_id: str
    transaction_id: str
    status: str = "active"
    checked_in_at: str | None = None


class FulfillmentService:
    """Issues and validates one single-use ticket for each paid order."""

    def __init__(self) -> None:
        self._tickets_by_order: dict[int, IssuedTicket] = {}
        self._tickets_by_code: dict[str, IssuedTicket] = {}
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
            self._tickets_by_code[ticket.ticket_code] = ticket
            return ticket

    def get_ticket_for_order(self, order_id: int) -> IssuedTicket | None:
        return self._tickets_by_order.get(order_id)

    def get_ticket_by_code(self, ticket_code: str) -> IssuedTicket | None:
        return self._tickets_by_code.get(ticket_code)

    def check_in(self, ticket_code: str) -> IssuedTicket:
        if not ticket_code:
            raise ValueError("ticket_code is required")

        with self._lock:
            ticket = self._tickets_by_code.get(ticket_code)
            if ticket is None:
                raise LookupError("ticket not found")
            if ticket.status == "checked_in":
                raise RuntimeError("ticket has already been checked in")
            if ticket.status != "active":
                raise RuntimeError("ticket is not active")

            checked_in_ticket = replace(
                ticket,
                status="checked_in",
                checked_in_at=datetime.now(timezone.utc).isoformat(),
            )
            self._tickets_by_code[ticket_code] = checked_in_ticket
            self._tickets_by_order[ticket.order_id] = checked_in_ticket
            return checked_in_ticket

    @staticmethod
    def serialize(ticket: IssuedTicket) -> dict:
        return asdict(ticket)


fulfillment_service = FulfillmentService()
