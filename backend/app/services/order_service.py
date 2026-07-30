from dataclasses import dataclass
from datetime import datetime, timezone
from threading import Lock


@dataclass
class OrderRecord:
    order_id: int
    user_id: int
    event_id: int
    amount: float
    status: str = "pending"
    created_at: str | None = None


class OrderService:
    """Business layer for order lifecycle management."""

    def __init__(self):
        self._orders = {}
        self._lock = Lock()

    def create_order(self, *, order_id: int, user_id: int, event_id: int, amount: float):
        with self._lock:
            if order_id in self._orders:
                return self._orders[order_id]

            order = OrderRecord(
                order_id=order_id,
                user_id=user_id,
                event_id=event_id,
                amount=amount,
                created_at=datetime.now(timezone.utc).isoformat(),
            )
            self._orders[order_id] = order
            return order

    def mark_paid(self, order_id: int):
        with self._lock:
            order = self._orders.get(order_id)
            if order is None:
                raise LookupError("order not found")

            order.status = "paid"
            return order


order_service = OrderService()
