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

### Changed

- README now distinguishes implemented, tested, deployed, and verified work.
- Repository documentation now treats GitHub as the project memory and single source of truth.

### Known limitations

- Current-head CI and tests are not yet verified.
- Complete Alembic migration path is not yet verified.
- Telegram, payment provider, VPS, DNS, TLS, backup restore, rollback, and UAT are not verified in target environments.

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
