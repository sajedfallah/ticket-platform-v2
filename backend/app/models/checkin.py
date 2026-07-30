from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.database.base import Base

class Checkin(Base):
    __tablename__ = "checkins"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ticket_id: Mapped[int] = mapped_column(Integer)
    scanner_user: Mapped[str] = mapped_column(String(100))
    checked_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
