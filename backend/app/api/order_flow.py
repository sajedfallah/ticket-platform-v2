from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.services.mvp_flow_service import mvp_flow_service

router = APIRouter(prefix="/orders", tags=["orders"])


class CreateOrderPayload(BaseModel):
    user_id: int = Field(gt=0)
    event_id: int = Field(gt=0)
    ticket_type_id: int = Field(gt=0)
    quantity: int = Field(default=1, gt=0, le=10)


@router.post("", status_code=status.HTTP_201_CREATED)
@router.post("/create", status_code=status.HTTP_201_CREATED, include_in_schema=False)
def create_order(payload: CreateOrderPayload):
    try:
        order = mvp_flow_service.create_order(**payload.model_dump())
    except LookupError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc

    return mvp_flow_service.serialize(order)


@router.get("/{order_id}")
def get_order(order_id: int):
    order = mvp_flow_service.get_order(order_id)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="order_not_found")
    return mvp_flow_service.serialize(order)
