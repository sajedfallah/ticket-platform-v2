from fastapi import APIRouter

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/create")
def create_order(payload: dict):
    return {
        "order_status": "pending",
        "payment_status": "pending",
        "data": payload
    }

@router.get("/{order_id}")
def get_order(order_id: int):
    return {"order_id": order_id, "status": "pending"}
