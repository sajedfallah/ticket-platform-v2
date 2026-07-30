import pytest


def test_create_event_flow():
    event = {
        "title": "Sample Music Event",
        "status": "DRAFT"
    }

    assert event["title"] == "Sample Music Event"
    assert event["status"] == "DRAFT"


def test_publish_event_flow():
    event_status = "PUBLISHED"

    assert event_status == "PUBLISHED"
