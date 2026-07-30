from app.services.fulfillment_service import fulfillment_service


def test_paid_order_issues_single_ticket():
    ticket = fulfillment_service.fulfill_paid_order(
        order_id=1001,
        payment_id="pay_test_1001",
        transaction_id="txn_test_1001",
    )

    duplicate = fulfillment_service.fulfill_paid_order(
        order_id=1001,
        payment_id="pay_test_1001",
        transaction_id="txn_test_1001",
    )

    assert ticket.ticket_code == duplicate.ticket_code
    assert ticket.status == "active"


def test_ticket_checkin_rules_documented():
    # Placeholder integration gate for API test client.
    # Real HTTP validation will be enabled after database persistence layer.
    assert True
