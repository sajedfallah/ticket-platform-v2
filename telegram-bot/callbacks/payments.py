"""Payment callback handlers."""


def handle_payment(order_id: int):
    return {"action": "pay_order", "order_id": order_id}


def handle_cancel(order_id: int):
    return {"action": "cancel_order", "order_id": order_id}
