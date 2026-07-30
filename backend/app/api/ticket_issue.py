from fastapi import APIRouter
from app.services.qr_service import generate_ticket_code

router = APIRouter(prefix="/tickets", tags=["tickets"])

@router.post("/issue")
def issue_ticket(payload: dict):
    code = generate_ticket_code()
    return {
        "ticket_code": code,
        "status": "active",
        "payload": payload
    }

@router.post("/check")
def check_ticket(payload: dict):
    return {"valid": True, "ticket": payload}
