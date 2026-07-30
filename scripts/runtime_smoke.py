from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from pathlib import Path

BACKEND = "http://localhost:8000"
MINI_APP = "http://localhost:8080"
REPORT = Path("runtime-smoke-local.json")


def request(method: str, url: str, payload: dict | None = None) -> dict | str:
    data = None
    headers: dict[str, str] = {}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=15) as response:
        content_type = response.headers.get("Content-Type", "")
        body = response.read().decode("utf-8")
        if "application/json" in content_type:
            return json.loads(body)
        return body


def wait_for_health(timeout_seconds: int = 180) -> dict:
    deadline = time.monotonic() + timeout_seconds
    last_error: Exception | None = None
    while time.monotonic() < deadline:
        try:
            result = request("GET", f"{BACKEND}/health")
            if isinstance(result, dict) and result.get("status") == "ok":
                return result
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            last_error = exc
        time.sleep(3)
    raise RuntimeError(f"Backend did not become healthy: {last_error}")


def main() -> None:
    evidence: dict[str, object] = {}

    evidence["health"] = wait_for_health()

    events = request("GET", f"{BACKEND}/api/events")
    assert isinstance(events, dict)
    assert events.get("items"), events
    event = events["items"][0]
    evidence["event"] = event

    order = request(
        "POST",
        f"{BACKEND}/api/orders",
        {
            "user_id": 1001,
            "event_id": event["id"],
            "ticket_type_id": event["ticket_type_id"],
            "quantity": 1,
        },
    )
    assert isinstance(order, dict)
    evidence["order"] = order

    payment = request(
        "POST",
        f"{BACKEND}/api/payments/create",
        {
            "order_id": order["id"],
            "callback_url": f"{MINI_APP}/payment-result",
        },
    )
    assert isinstance(payment, dict)
    evidence["payment"] = payment

    verified = request(
        "POST",
        f"{BACKEND}/api/payments/verify",
        {"payment_id": payment["payment_id"], "success": True},
    )
    assert isinstance(verified, dict)
    assert verified.get("order_status") == "paid", verified
    ticket = verified.get("ticket")
    assert isinstance(ticket, dict) and ticket.get("status") == "active", verified
    evidence["verification"] = verified

    checked_in = request(
        "POST",
        f"{BACKEND}/api/tickets/check-in",
        {"ticket_code": ticket["ticket_code"]},
    )
    assert isinstance(checked_in, dict)
    assert checked_in.get("entry_allowed") is True, checked_in
    evidence["check_in"] = checked_in

    mini_app_html = request("GET", f"{MINI_APP}/")
    assert isinstance(mini_app_html, str) and '<div id="root"></div>' in mini_app_html
    evidence["mini_app"] = "reachable"

    REPORT.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Runtime smoke passed.")
    print(f"Evidence written to {REPORT}")


if __name__ == "__main__":
    main()
