# Database Migrations

This directory contains database migration notes and Alembic migration history.

Migration flow:

1. Update SQLAlchemy models.
2. Generate Alembic revision.
3. Review migration.
4. Apply with `alembic upgrade head`.

Production database changes must be applied through migrations only.