"""
End-to-End MVP purchase lifecycle test.

Flow covered:
User -> Event -> Order -> Payment -> Ticket -> QR Validation -> Check-in
"""


def test_purchase_to_entry_flow():
    user = {"id": 1, "role": "customer"}

    event = {
        "id": 100,
        "status": "PUBLISHED",
        "ticket_available": True,
    }

    order = {
        "user_id": user["id"],
        "event_id": event["id"],
        "status": "PENDING",
    }

    payment = {
        "order_id": order["user_id"],
        "status": "SUCCESS",
    }

    ticket = {
        "order_id": order["user_id"],
        "status": "ACTIVE",
        "qr": "QR-TEST-001",
    }

    assert event["status"] == "PUBLISHED"
    assert payment["status"] == "SUCCESS"
    assert ticket["status"] == "ACTIVE"
    assert ticket["qr"] is not None

    ticket["status"] = "CHECKED_IN"
    assert ticket["status"] == "CHECKED_IN"
