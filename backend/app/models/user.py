from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[str | None] = mapped_column(String(50), unique=True)
    username: Mapped[str | None] = mapped_column(String(100))
    phone: Mapped[str | None] = mapped_column(String(30))
    role: Mapped[str] = mapped_column(default="customer")
    status: Mapped[str] = mapped_column(default="active")
