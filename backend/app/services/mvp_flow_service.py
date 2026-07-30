from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from threading import Lock
from uuid import uuid4


@dataclass(frozen=True)
class EventRecord:
    id: int
    title: str
    description: str
    category: str
    status: str
    ticket_type_id: int
    ticket_name: str
    ticket_price: int
    currency: str
    capacity: int


@dataclass(frozen=True)
class OrderRecord:
    id: int
    order_number: str
    user_id: int
    event_id: int
    ticket_type_id: int
    quantity: int
    unit_price: int
    total_amount: int
    currency: str
    status: str = "pending"
    payment_id: str | None = None


class MVPFlowService:
    """Small in-memory product flow used until database repositories are wired."""

    def __init__(self) -> None:
        self._lock = Lock()
        self._events: dict[int, EventRecord] = {}
        self._orders: dict[int, OrderRecord] = {}
        self._next_event_id = 1
        self._next_ticket_type_id = 1
        self._next_order_id = 1
        self._seed_demo_event()

    def _seed_demo_event(self) -> None:
        self.create_event(
            title="Ticket Platform Demo Event",
            description="A demo event for the first complete ticket-purchase journey.",
            category="demo",
            ticket_name="General Admission",
            ticket_price=2500,
            currency="EUR",
            capacity=100,
            status="published",
        )

    def create_event(
        self,
        *,
        title: str,
        description: str,
        category: str,
        ticket_name: str,
        ticket_price: int,
        currency: str,
        capacity: int,
        status: str = "draft",
    ) -> EventRecord:
        with self._lock:
            event = EventRecord(
                id=self._next_event_id,
                title=title,
                description=description,
                category=category,
                status=status,
                ticket_type_id=self._next_ticket_type_id,
                ticket_name=ticket_name,
                ticket_price=ticket_price,
                currency=currency.upper(),
                capacity=capacity,
            )
            self._events[event.id] = event
            self._next_event_id += 1
            self._next_ticket_type_id += 1
            return event

    def list_events(self) -> list[EventRecord]:
        return list(self._events.values())

    def get_event(self, event_id: int) -> EventRecord | None:
        return self._events.get(event_id)

    def create_order(
        self,
        *,
        user_id: int,
        event_id: int,
        ticket_type_id: int,
        quantity: int,
    ) -> OrderRecord:
        event = self.get_event(event_id)
        if event is None:
            raise LookupError("event_not_found")
        if event.status != "published":
            raise RuntimeError("event_not_available")
        if event.ticket_type_id != ticket_type_id:
            raise LookupError("ticket_type_not_found")
        if quantity <= 0:
            raise ValueError("quantity_must_be_positive")
        if quantity > event.capacity:
            raise RuntimeError("insufficient_capacity")

        with self._lock:
            order = OrderRecord(
                id=self._next_order_id,
                order_number=f"ORD-{uuid4().hex[:12].upper()}",
                user_id=user_id,
                event_id=event_id,
                ticket_type_id=ticket_type_id,
                quantity=quantity,
                unit_price=event.ticket_price,
                total_amount=event.ticket_price * quantity,
                currency=event.currency,
            )
            self._orders[order.id] = order
            self._next_order_id += 1
            return order

    def get_order(self, order_id: int) -> OrderRecord | None:
        return self._orders.get(order_id)

    def attach_payment(self, order_id: int, payment_id: str) -> OrderRecord:
        return self._update_order(order_id, payment_id=payment_id, status="payment_pending")

    def mark_paid(self, order_id: int, payment_id: str) -> OrderRecord:
        return self._update_order(order_id, payment_id=payment_id, status="paid")

    def mark_payment_failed(self, order_id: int, payment_id: str) -> OrderRecord:
        return self._update_order(order_id, payment_id=payment_id, status="payment_failed")

    def _update_order(self, order_id: int, **changes: object) -> OrderRecord:
        with self._lock:
            order = self._orders.get(order_id)
            if order is None:
                raise LookupError("order_not_found")
            updated = replace(order, **changes)
            self._orders[order_id] = updated
            return updated

    @staticmethod
    def serialize(record: EventRecord | OrderRecord) -> dict:
        return asdict(record)


mvp_flow_service = MVPFlowService()
