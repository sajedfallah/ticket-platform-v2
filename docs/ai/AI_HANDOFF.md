# AI Handoff

## Objective

Stabilize the repository, preserve truthful project memory, and verify the backend and database lifecycle before any new feature or VPS deployment work.

## Work Completed

- Established repository-first documentation, Current Project State, architecture, roadmap, AI context, bootstrap, master prompt, and handoff files.
- Audited and repaired the backend GitHub Actions workflow paths and test dependencies.
- Replaced placeholder check-in coverage with real assertions for idempotent issuance, single-use check-in, and unknown-ticket rejection.
- Confirmed that no current-head CI status was available through the GitHub connector.
- Replaced the Alembic placeholder with executable online/offline migration support driven by `DATABASE_URL`.
- Removed fixed sample database credentials from `backend/alembic.ini`.
- Inventoried the complete current model set: users, events, venues, ticket types, orders, payments, discounts, order items, tickets, and check-ins.
- Added the reviewed initial revision `backend/migrations/versions/20260730_0001_initial_schema.py`.
- Updated Current Project State and CHANGELOG with the exact evidence level and remaining limitations.

## Files Changed or Added

- `.github/workflows/backend-test.yml`
- `backend/requirements-dev.txt`
- `tests/integration/test_payment_ticket_checkin_flow.py`
- `backend/alembic.ini`
- `backend/migrations/env.py`
- `backend/migrations/README.md`
- `backend/migrations/versions/20260730_0001_initial_schema.py`
- `docs/project/current-state.md`
- `CHANGELOG.md`
- `docs/ai/AI_HANDOFF.md`
- Repository governance and architecture documents listed in `docs/index.md`

## Key Findings

- The repository is pre-beta, not a verified beta release.
- No passing current-head CI result has been recorded.
- The original CI workflow used incorrect root paths and omitted an explicit pytest dependency.
- The original Alembic environment was not executable.
- The initial migration now exists and mirrors the constraints explicitly declared by the current models.
- Multiple relational-looking columns are plain integers without Foreign Key constraints. The migration intentionally preserves that current model behavior instead of inventing relationships.
- Backend, persistence, payment/ticket/check-in, Docker, Nginx, and Certbot foundations exist, but target-environment verification remains incomplete.

## Verification Performed

- Inspected repository metadata, recent commits, combined commit status, workflow, requirements, application bootstrap, fulfillment service, tests, Alembic configuration, and every current SQLAlchemy model through the GitHub connector.
- Compared migration table definitions with current model columns, nullable behavior, unique constraints, the ticket-code index, and the one declared Foreign Key from tickets to orders.
- Corrected evidence-backed CI, test, and Alembic defects.

## Tests Not Yet Executed or Proven Passing

- Corrected GitHub Actions backend workflow on current head
- Local clean-environment backend test run
- Clean PostgreSQL `alembic upgrade head`
- `alembic downgrade base` followed by re-upgrade
- Fresh autogenerate comparison for schema drift
- Database-backed API integration tests
- Concurrent check-in protection
- Docker Compose build and health checks
- Telegram bot and Mini App builds
- Admin panel build
- Real payment-provider flow
- VPS/DNS/TLS deployment
- Backup restore and rollback
- End-to-end UAT

## Current Blockers

- No passing current-head CI result has been recorded.
- No clean PostgreSQL migration evidence exists.
- No migration downgrade/re-upgrade evidence exists.
- No target VPS or domain execution evidence exists.
- No real Telegram or payment-provider configuration exists.
- Authentication and authorization require audit.

## Exact Next Action

Using a disposable PostgreSQL database and non-production credentials:

1. From `backend/`, export `DATABASE_URL`.
2. Run `alembic upgrade head`.
3. Inspect that all ten expected tables and the ticket-code index exist.
4. Run `alembic downgrade base`.
5. Run `alembic upgrade head` again.
6. Run a temporary `alembic revision --autogenerate` and confirm it contains no unintended schema changes; do not keep an empty comparison revision.
7. Run the backend test suite.
8. Record exact outputs and update Current Project State, CHANGELOG, and this handoff.

Do not mark migrations `TESTED` until these commands succeed on PostgreSQL. Do not add missing Foreign Keys silently; model and domain changes require an ADR and coordinated model/migration updates.

## Required Human Inputs for Later Deployment

- Domain and DNS access
- VPS IP, OS, and SSH user
- BotFather configuration
- Payment provider and sandbox credentials
- Business rules for refunds, settlements, and organizer onboarding

Never place secrets in GitHub files, issues, commits, or chat.
