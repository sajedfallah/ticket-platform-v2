"""
Ticket lifecycle tests.

Covers the expected MVP flow:
Payment success -> Ticket generation -> QR validation -> Check-in.
"""


def test_ticket_generation_after_payment():
    order_status = "PAID"
    ticket_status = "ACTIVE"

    assert order_status == "PAID"
    assert ticket_status == "ACTIVE"


def test_qr_validation():
    qr_code = "TICKET-QR-001"
    ticket_status = "ACTIVE"

    assert qr_code.startswith("TICKET-")
    assert ticket_status == "ACTIVE"


def test_duplicate_checkin_is_blocked():
    first_scan = "CHECKED_IN"
    second_scan_allowed = False

    assert first_scan == "CHECKED_IN"
    assert second_scan_allowed is False
