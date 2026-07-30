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
- Upgraded `.github/workflows/backend-test.yml` into `Backend Verification` with PostgreSQL 16, migration lifecycle checks, backend compilation, pytest, and manual dispatch.
- Found and fixed an Alembic startup defect: `env.py` invoked `fileConfig` even though the minimal `alembic.ini` has no logging sections. Logging setup is now conditional.
- Updated Current Project State and CHANGELOG with exact evidence levels and verification limitations.

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
- The initial migration exists and mirrors constraints explicitly declared by current models.
- Multiple relational-looking columns are plain integers without Foreign Key constraints. The migration intentionally preserves current model behavior instead of inventing relationships.
- The GitHub Actions workflow defines real PostgreSQL migration lifecycle checks, but no successful run or logs have been recorded yet.
- The GitHub connector view used here returned no pull-request-triggered runs for the inspected commits.
- The local audit runtime could not clone GitHub because DNS resolution for `github.com` was unavailable.
- Backend, persistence, payment/ticket/check-in, Docker, Nginx, and Certbot foundations exist, but target-environment verification remains incomplete.

## Verification Performed

- Inspected repository metadata, recent commits, combined commit status, workflow, requirements, application bootstrap, fulfillment service, tests, Alembic configuration, and all current SQLAlchemy models through the GitHub connector.
- Compared migration definitions with model columns, nullability, unique constraints, the ticket-code index, and the declared ticket-to-order Foreign Key.
- Performed static inspection of Alembic startup behavior and corrected the invalid unconditional logging initialization.
- Attempted an independent clone-and-run verification, but the runtime could not resolve GitHub.

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
- The available connector does not expose the needed push-based run evidence.
- The local audit runtime cannot currently clone GitHub.
- No target VPS or domain execution evidence exists.
- No real Telegram or payment-provider configuration exists.
- Authentication and authorization require audit.

## Exact Next Action

1. Manually dispatch `Backend Verification` on the latest `main` head.
2. Retrieve the first failing job step and its log.
3. If a step fails, fix only the observed root cause and re-run verification.
4. If all migration and pytest steps pass, update `docs/project/current-state.md` to mark the covered migration lifecycle and service behaviors as `TESTED`.
5. Preserve the run URL or identifiers and exact result in this handoff and the changelog.
6. Only then continue to Docker health checks and fail-fast deployment.

Do not mark migrations or tests `TESTED` without a successful PostgreSQL-backed workflow result. Do not add missing Foreign Keys silently; model and domain changes require an ADR and coordinated model/migration updates.

## Required Human Inputs for Later Deployment

- Domain and DNS access
- VPS IP, OS, and SSH user
- BotFather configuration
- Payment provider and sandbox credentials
- Business rules for refunds, settlements, and organizer onboarding

Never place secrets in GitHub files, issues, commits, or chat.
