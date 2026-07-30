from sqlalchemy import Column, Integer, String, Float
from app.database.base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    event_id = Column(Integer, nullable=False)
    ticket_type_id = Column(Integer, nullable=True)
    order_number = Column(String, unique=True, nullable=False)
    total_amount = Column(Float, default=0)
    status = Column(String, default="pending")
