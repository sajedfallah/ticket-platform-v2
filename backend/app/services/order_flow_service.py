from sqlalchemy.orm import Session


def create_order_flow(db: Session, order_data):
    """MVP order lifecycle.

    Flow:
    create order -> reserve capacity -> payment pending -> ticket issue
    """
    return {
        "status": "pending",
        "order": order_data,
    }
