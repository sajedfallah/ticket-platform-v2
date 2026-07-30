from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Venue(Base):
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    capacity = Column(Integer, default=0)
