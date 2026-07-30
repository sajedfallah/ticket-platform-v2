from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    ticket_code: Mapped[str] = mapped_column(String(100), unique=True)
    qr_code: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(default="active")
