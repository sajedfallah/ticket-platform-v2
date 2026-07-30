import pytest

from app.services.fulfillment_service import FulfillmentService


def test_paid_order_issues_single_ticket():
    service = FulfillmentService()

    ticket = service.fulfill_paid_order(
        order_id=1001,
        payment_id="pay_test_1001",
        transaction_id="txn_test_1001",
    )

    duplicate = service.fulfill_paid_order(
        order_id=1001,
        payment_id="pay_test_1001",
        transaction_id="txn_test_1001",
    )

    assert ticket.ticket_code == duplicate.ticket_code
    assert ticket.status == "active"


def test_ticket_can_be_checked_in_only_once():
    service = FulfillmentService()
    ticket = service.fulfill_paid_order(
        order_id=2001,
        payment_id="pay_test_2001",
        transaction_id="txn_test_2001",
    )

    checked_in = service.check_in(ticket.ticket_code)

    assert checked_in.status == "checked_in"
    assert checked_in.checked_in_at is not None

    with pytest.raises(RuntimeError, match="already been checked in"):
        service.check_in(ticket.ticket_code)


def test_unknown_ticket_cannot_be_checked_in():
    service = FulfillmentService()

    with pytest.raises(LookupError, match="ticket not found"):
        service.check_in("missing-ticket-code")
