from sqlalchemy import Column, Integer, String, Float
from app.database.base import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    payment_id = Column(String, unique=True, nullable=True)
    transaction_id = Column(String, nullable=True)
    status = Column(String, default="pending")
