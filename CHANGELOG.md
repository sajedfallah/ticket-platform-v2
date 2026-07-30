# Changelog

All notable changes to Ticket Platform v2 are recorded here.

The project uses semantic versioning where practical. Pre-release status does not imply production readiness.

## [0.2.0-prebeta] - 2026-07-31

### Added

- Repository memory, architecture, roadmap, AI bootstrap, master prompt, and handoff documentation
- Backend development test requirements and PostgreSQL-backed verification workflow
- Executable Alembic environment and reviewed initial migration
- Reusable backend verification script with Summary and retained artifact reporting
- `MVPFlowService` with a seeded published event and process-local event/order state
- Event list, detail, and create API behavior
- Validated order creation and lookup with quantity, capacity, amount, and currency calculation
- Mock payment flow tied to actual order amount and status
- First complete service-level purchase test covering event → order → payment → ticket → check-in

### Changed

- Events and order endpoints no longer return placeholder responses.
- Payment creation now requires an existing payable order and derives amount/currency from it.
- Payment verification now updates the matching order before ticket fulfillment.
- README and project-state documents distinguish implemented, tested, deployed, and verified work.
- Alembic uses environment-driven credentials and safely handles minimal logging configuration.

### Known limitations

- The executable MVP product flow is currently in memory and loses data on backend restart.
- Process-local state is not safe for multiple workers or production deployment.
- A passing current-head CI result is not yet recorded.
- Database-backed API integration, concurrent check-in, Telegram authentication, real payment, VPS, DNS, TLS, backup restore, rollback, and UAT remain unverified.
- Several relational-looking model columns remain without Foreign Key constraints.

## Historical Work Before Documentation Baseline

The repository contains earlier foundations for FastAPI, SQLAlchemy models, order/payment/ticket/check-in services, Telegram components, Docker Compose, Nginx, Certbot, deployment runbooks, and beta UAT planning. Historical work is not automatically considered tested, deployed, or verified. Refer to `docs/project/current-state.md` for current evidence levels.
