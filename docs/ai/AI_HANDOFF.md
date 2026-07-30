# AI Handoff

## Objective

Stabilize the repository, preserve truthful project memory, and verify the backend and database lifecycle before any new feature or VPS deployment work.

## Work Completed

- Established repository-first documentation, Current Project State, architecture, roadmap, AI context, bootstrap, master prompt, and handoff files.
- Audited and repaired backend CI paths and explicit test dependencies.
- Replaced placeholder check-in coverage with real assertions for idempotent issuance, single-use check-in, and unknown-ticket rejection.
- Replaced the Alembic placeholder with executable online/offline migration support driven by `DATABASE_URL`.
- Removed fixed sample database credentials from `backend/alembic.ini`.
- Inventoried the complete current model set and added `backend/migrations/versions/20260730_0001_initial_schema.py`.
- Upgraded `.github/workflows/backend-test.yml` into `Backend Verification` with:
  - an ephemeral PostgreSQL 16 service;
  - database health checks;
  - clean `alembic upgrade head`;
  - `alembic current`;
  - `alembic check` for schema drift;
  - `alembic downgrade base`;
  - re-upgrade to head;
  - backend compilation and pytest execution;
  - manual `workflow_dispatch` support.
- Updated Current Project State and CHANGELOG with exact evidence levels.

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
- The initial migration now exists and mirrors constraints explicitly declared by current models.
- Multiple relational-looking columns are plain integers without Foreign Key constraints. The migration intentionally preserves current model behavior instead of inventing relationships.
- The GitHub Actions workflow now defines real PostgreSQL migration lifecycle checks, but no successful run or logs have been recorded yet.
- Backend, persistence, payment/ticket/check-in, Docker, Nginx, and Certbot foundations exist, but target-environment verification remains incomplete.

## Verification Performed

- Inspected repository metadata, recent commits, combined commit status, workflow, requirements, application bootstrap, fulfillment service, tests, Alembic configuration, and all current SQLAlchemy models through the GitHub connector.
- Compared migration definitions with model columns, nullability, unique constraints, the ticket-code index, and the declared ticket-to-order Foreign Key.
- Confirmed that the latest inspected commit had no returned status checks at inspection time.
- Corrected evidence-backed CI, test, and Alembic defects.

## Tests Not Yet Executed or Proven Passing

- `Backend Verification` workflow on current head
- PostgreSQL 16 clean `alembic upgrade head`
- `alembic check` with no schema drift
- `alembic downgrade base` followed by re-upgrade
- Backend pytest execution in GitHub Actions
- Database-backed API integration tests
- Concurrent check-in protection
- Docker Compose build and application health checks
- Telegram bot and Mini App builds
- Admin panel build
- Real payment-provider flow
- VPS/DNS/TLS deployment
- Backup restore and rollback
- End-to-end UAT

## Current Blockers

- No passing current-head `Backend Verification` result has been recorded.
- No workflow job logs have been inspected for the PostgreSQL migration lifecycle.
- No target VPS or domain execution evidence exists.
- No real Telegram or payment-provider configuration exists.
- Authentication and authorization require audit.

## Exact Next Action

1. Observe or manually dispatch the `Backend Verification` workflow for commit `52f8f14c51f0676fdaa8fc09d6394d4100c19d09` or the latest documentation head.
2. Retrieve the workflow jobs and logs.
3. If a step fails, identify the first root cause and make the smallest coherent repair.
4. Re-run verification.
5. If all migration and pytest steps pass, update `docs/project/current-state.md` to mark the covered migration lifecycle and service behaviors as `TESTED`.
6. Preserve the run URL or identifiers and exact result in this handoff and the changelog.
7. Only then continue to Docker health checks and fail-fast deployment.

Do not mark migrations or tests `TESTED` without a successful PostgreSQL-backed workflow result. Do not add missing Foreign Keys silently; model and domain changes require an ADR and coordinated model/migration updates.

## Required Human Inputs for Later Deployment

- Domain and DNS access
- VPS IP, OS, and SSH user
- BotFather configuration
- Payment provider and sandbox credentials
- Business rules for refunds, settlements, and organizer onboarding

Never place secrets in GitHub files, issues, commits, or chat.
