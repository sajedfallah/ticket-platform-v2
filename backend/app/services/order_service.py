class OrderService:
    """Business logic for ticket orders."""

    def create_order(self, user_id: int, event_id: int, amount: float) -> dict:
        return {
            "user_id": user_id,
            "event_id": event_id,
            "amount": amount,
            "status": "pending"
        }
