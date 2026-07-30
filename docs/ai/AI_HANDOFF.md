# AI Handoff

## Objective

Stabilize the repository, establish truthful project memory, and verify the backend and database lifecycle before any new feature or VPS deployment work.

## Work Completed

- Established repository-first documentation, Current Project State, architecture, roadmap, AI context, bootstrap, master prompt, and handoff files.
- Audited and repaired the backend GitHub Actions workflow paths and test dependencies.
- Replaced placeholder check-in coverage with real assertions for idempotent issuance, single-use check-in, and unknown-ticket rejection.
- Checked the latest commit status and found no registered CI statuses available through the connector.
- Audited Alembic and found that `backend/migrations/env.py` was a non-executable placeholder and `backend/alembic.ini` contained a fixed sample credential URL.
- Replaced the Alembic placeholder with online/offline migration execution, environment-driven `DATABASE_URL`, logging support, schema comparison options, and explicit imports for all known model modules.
- Removed fixed database credentials from `alembic.ini`.
- Expanded the migration runbook with safe generation, review, upgrade, downgrade, and evidence requirements.

## Files Changed or Added

- `.github/workflows/backend-test.yml`
- `backend/requirements-dev.txt`
- `tests/integration/test_payment_ticket_checkin_flow.py`
- `backend/alembic.ini`
- `backend/migrations/env.py`
- `backend/migrations/README.md`
- `docs/project/current-state.md`
- `CHANGELOG.md`
- `docs/ai/AI_HANDOFF.md`
- Repository governance and architecture documents listed in `docs/index.md`

## Key Findings

- The repository is pre-beta, not a verified beta release.
- No current-head GitHub status checks were returned for the latest inspected commit.
- The original CI workflow used incorrect root-level paths and omitted an explicit pytest dependency.
- The previous Alembic environment could not run migrations because it lacked Alembic context configuration and execution functions.
- No reviewed initial migration revision chain is currently proven.
- Backend, persistence, payment/ticket/check-in, Docker, Nginx, and Certbot foundations exist, but target-environment verification remains incomplete.

## Verification Performed

- Inspected repository metadata, recent commits, combined commit status, CI workflow, requirements, application bootstrap, fulfillment service, tests, Alembic configuration, migration environment, and model-history evidence through the GitHub connector.
- Confirmed no status checks were registered for the latest inspected commit.
- Corrected evidence-backed CI, test, and Alembic defects.

## Tests Not Yet Executed or Proven Passing

- Corrected GitHub Actions backend workflow on current head
- Local clean-environment backend test run
- Initial Alembic revision generation and manual review
- Clean PostgreSQL `alembic upgrade head`
- Alembic downgrade/upgrade verification
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
- No reviewed initial Alembic revision exists.
- No clean PostgreSQL migration evidence exists.
- No target VPS or domain execution evidence exists.
- No real Telegram or payment-provider configuration exists.
- Authentication and authorization require audit.

## Exact Next Action

From a disposable environment with PostgreSQL available:

1. Run from `backend/` with a non-production `DATABASE_URL`.
2. Execute `alembic revision --autogenerate -m "initial schema"`.
3. Review every generated table, column, index, unique constraint, and foreign key against the current SQLAlchemy models.
4. Apply `alembic upgrade head` to an empty database.
5. Run the backend tests.
6. Record exact command output and commit the reviewed revision only if successful.
7. Update `docs/project/current-state.md`, `CHANGELOG.md`, and this handoff with the evidence.

Do not fabricate a migration revision without comparing it to the complete current model set.

## Required Human Inputs for Later Deployment

- Domain and DNS access
- VPS IP, OS, and SSH user
- BotFather configuration
- Payment provider and sandbox credentials
- Business rules for refunds, settlements, and organizer onboarding

Never place secrets in GitHub files, issues, commits, or chat.
