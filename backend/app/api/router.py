from fastapi import APIRouter
from app.api.events import router as events_router
from app.api.tickets import router as tickets_router
from app.api.orders import router as orders_router
from app.api.payments import router as payments_router

api_router = APIRouter()

api_router.include_router(events_router)
api_router.include_router(tickets_router)
api_router.include_router(orders_router)
api_router.include_router(payments_router)
