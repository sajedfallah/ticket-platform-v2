from fastapi import APIRouter

router = APIRouter(prefix="/api/orders", tags=["Orders"])


@router.post("/create")
def create_order(payload: dict):
    return {
        "status": "pending",
        "message": "Order creation endpoint ready"
    }


@router.get("/{order_id}")
def get_order(order_id: int):
    return {
        "id": order_id,
        "message": "Order detail endpoint ready"
    }
