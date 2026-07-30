from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base

class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str | None] = mapped_column(Text)
    category: Mapped[str] = mapped_column(String(50))
    status: Mapped[str] = mapped_column(default="draft")
