# Database Migrations

Alembic is the only supported mechanism for production schema changes.

## Configuration

Run commands from `backend/` and provide the connection string through the environment:

```bash
export DATABASE_URL='postgresql://user:password@host:5432/ticket_platform'
alembic current
alembic history
```

Do not place real credentials in `alembic.ini`, source files, documentation, issues, or commits.

`migrations/env.py` imports every module in `app.models` so all registered tables are visible to Alembic autogeneration.

## Change Workflow

1. Update SQLAlchemy models.
2. Start from a disposable development database.
3. Generate a revision:

   ```bash
   alembic revision --autogenerate -m "describe schema change"
   ```

4. Review the generated `upgrade()` and `downgrade()` operations manually.
5. Apply from an empty database:

   ```bash
   alembic upgrade head
   ```

6. Verify the application can start and inspect the resulting schema.
7. Test rollback where safe:

   ```bash
   alembic downgrade -1
   alembic upgrade head
   ```

8. Commit the model, revision, tests, and affected documentation together.

## Current Repository Status

- Alembic configuration: `IMPLEMENTED`
- Environment-driven connection handling: `IMPLEMENTED`
- Model metadata registration: `IMPLEMENTED`
- Executable initial revision chain: `BLOCKED`
- Empty PostgreSQL upgrade verification: `NOT VERIFIED`
- Downgrade verification: `NOT VERIFIED`

Do not claim database migrations are tested until `alembic upgrade head` has succeeded against a clean PostgreSQL database and the evidence has been recorded in `docs/project/current-state.md`.
