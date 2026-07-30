from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base

class Discount(Base):
    __tablename__ = "discounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_id: Mapped[int] = mapped_column(Integer)
    code: Mapped[str] = mapped_column(String(50), unique=True)
    value: Mapped[float] = mapped_column(Float)
    max_usage: Mapped[int] = mapped_column(Integer, default=0)
