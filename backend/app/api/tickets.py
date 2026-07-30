from fastapi import APIRouter

router = APIRouter(prefix="/api/tickets", tags=["Tickets"])


@router.post("/check")
def check_ticket(payload: dict):
    return {
        "valid": False,
        "message": "Ticket validation endpoint ready"
    }


@router.post("/create")
def create_ticket(payload: dict):
    return {
        "status": "created",
        "message": "Ticket creation endpoint ready"
    }
