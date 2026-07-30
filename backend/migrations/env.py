from __future__ import annotations

import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from app.database.base import Base

# Import every model module so SQLAlchemy registers all tables in Base.metadata.
# Keep this list synchronized with backend/app/models.
from app.models import (  # noqa: F401
    checkin,
    discount,
    event,
    order,
    order_item,
    payment,
    ticket,
    ticket_type,
    user,
    venue,
)

config = context.config

# Only configure logging when the expected Alembic logging sections exist.
# The project intentionally keeps alembic.ini minimal and credential-free.
if config.config_file_name is not None and config.file_config.has_section("loggers"):
    fileConfig(config.config_file_name, disable_existing_loggers=False)


def get_database_url() -> str:
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError(
            "DATABASE_URL is required for Alembic migrations. "
            "Set it in the environment; never commit production credentials."
        )
    return database_url


config.set_main_option("sqlalchemy.url", get_database_url().replace("%", "%%"))
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    context.configure(
        url=get_database_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
        compare_server_default=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
