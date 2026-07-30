from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    ticket_code: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    qr_code: Mapped[str | None] = mapped_column(String(255), nullable=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    payment_id: Mapped[str] = mapped_column(String(100))
    transaction_id: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(default="active")
    checked_in_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
