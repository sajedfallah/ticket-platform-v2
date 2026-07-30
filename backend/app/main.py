from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.events_crud import router as events_router
from app.api.order_flow import router as orders_router
from app.api.ticket_issue import router as tickets_router
from app.api.payments import router as payments_router

app = FastAPI(
    title="Ticket Platform v2",
    version="0.2.0",
)

app.include_router(health_router)
app.include_router(events_router, prefix="/api")
app.include_router(orders_router, prefix="/api")
app.include_router(tickets_router, prefix="/api")
app.include_router(payments_router, prefix="/api")


@app.get("/")
def root():
    return {
        "status": "running",
        "service": "ticket-platform-backend",
        "version": "0.2.0",
    }
