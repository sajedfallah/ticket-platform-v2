# Changelog

All notable changes to Ticket Platform v2 are recorded here.

The project uses semantic versioning where practical. Pre-release status does not imply production readiness.

## [0.2.0-prebeta] - 2026-07-30

### Added

- Canonical documentation index
- Truthful Current Project State
- Evidence-based roadmap
- Architecture overview
- AI Context, Bootstrap Guide, Master Prompt, and Handoff
- Project `VERSION` file
- Backend development test requirements in `backend/requirements-dev.txt`
- Meaningful service-level tests for idempotent ticket issuance, single-use check-in, and unknown-ticket rejection
- Executable Alembic online/offline migration environment driven by `DATABASE_URL`
- Reviewed initial migration revision in `backend/migrations/versions/20260730_0001_initial_schema.py`
- PostgreSQL 16 service in GitHub Actions for clean migration lifecycle verification
- CI steps for Alembic upgrade, current-head inspection, schema-drift check, downgrade to base, re-upgrade, and backend tests
- Manual `workflow_dispatch` support for backend verification
- Reusable `backend/scripts/verify_backend.sh` verification entry point
- Markdown verification report with first-failure capture
- GitHub Actions Summary publishing and 30-day verification artifact retention

### Changed

- README now distinguishes implemented, tested, deployed, and verified work.
- Repository documentation now treats GitHub as the project memory and single source of truth.
- Backend GitHub Actions workflow now runs from the correct `backend/` directory.
- CI now installs explicit test dependencies, compiles backend and migration code, and runs tests with the correct `PYTHONPATH`.
- Placeholder check-in coverage was replaced with real assertions.
- Alembic no longer contains a fixed sample credential URL and now requires environment configuration.
- Alembic logging initialization is skipped safely when the minimal configuration has no logging sections.
- Migration documentation now defines review, upgrade, downgrade, and evidence requirements.
- Backend CI was renamed to `Backend Verification` to reflect migration and test coverage.
- CI now delegates verification to one reusable script rather than duplicating commands in workflow YAML.

### Known limitations

- A passing current-head CI result is not yet recorded.
- The PostgreSQL migration workflow is implemented but its successful execution has not been verified.
- Several relational-looking columns remain without Foreign Key constraints because current SQLAlchemy models do not declare them.
- Telegram, payment provider, VPS, DNS, TLS, backup restore, rollback, and UAT are not verified in target environments.
- Service-level tests do not yet verify real database-backed API transactions or concurrent check-in behavior.

## Historical Work Before Documentation Baseline

The repository contains earlier foundations for:

- FastAPI backend and API routers
- SQLAlchemy models and services
- Orders, payments, ticket fulfillment, and QR check-in
- Integration-test coverage foundation
- GitHub Actions backend CI
- Docker Compose production deployment
- Nginx routing and Certbot TLS bootstrap
- VPS and beta UAT runbooks

Historical work is not automatically considered tested, deployed, or verified. Refer to `docs/project/current-state.md` for current evidence levels.
