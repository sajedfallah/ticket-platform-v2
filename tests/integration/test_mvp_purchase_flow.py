from app.payments.provider import PaymentRequest, PaymentStatus, MockPaymentProvider
from app.services.fulfillment_service import FulfillmentService
from app.services.mvp_flow_service import MVPFlowService


def test_first_complete_purchase_journey():
    flow = MVPFlowService()
    payments = MockPaymentProvider()
    fulfillment = FulfillmentService()

    event = flow.list_events()[0]
    order = flow.create_order(
        user_id=101,
        event_id=event.id,
        ticket_type_id=event.ticket_type_id,
        quantity=2,
    )

    assert order.total_amount == event.ticket_price * 2
    assert order.status == "pending"

    payment = payments.create_payment(
        PaymentRequest(
            order_id=order.id,
            amount=order.total_amount,
            callback_url="https://example.test/payment/callback",
            currency=order.currency,
        )
    )
    flow.attach_payment(order.id, payment.payment_id)

    result = payments.verify_payment(payment.payment_id, success=True)
    assert result.status is PaymentStatus.PAID

    paid_order = flow.mark_paid(order.id, payment.payment_id)
    ticket = fulfillment.fulfill_paid_order(
        order_id=order.id,
        payment_id=payment.payment_id,
        transaction_id=result.transaction_id or "",
    )

    assert paid_order.status == "paid"
    assert ticket.order_id == order.id
    assert ticket.status == "active"

    checked_in = fulfillment.check_in(ticket.ticket_code)
    assert checked_in.status == "checked_in"
    assert checked_in.checked_in_at is not None


def test_order_rejects_unknown_event_and_ticket_type():
    flow = MVPFlowService()
    event = flow.list_events()[0]

    try:
        flow.create_order(user_id=1, event_id=999, ticket_type_id=1, quantity=1)
    except LookupError as exc:
        assert str(exc) == "event_not_found"
    else:
        raise AssertionError("unknown event should fail")

    try:
        flow.create_order(user_id=1, event_id=event.id, ticket_type_id=999, quantity=1)
    except LookupError as exc:
        assert str(exc) == "ticket_type_not_found"
    else:
        raise AssertionError("unknown ticket type should fail")
