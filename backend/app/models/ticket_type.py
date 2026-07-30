from sqlalchemy import Column, Integer, String, Float
from app.database.base import Base

class TicketType(Base):
    __tablename__ = "ticket_types"

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    capacity = Column(Integer, default=0)
    sold_count = Column(Integer, default=0)
