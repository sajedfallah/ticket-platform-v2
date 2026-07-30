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
- React/Vite Persian RTL Telegram Mini App under `mini-app/`
- Connected Mini App journey for event selection, quantity, order creation, mock payment, ticket issuance, and QR display
- Telegram WebApp SDK initialization and optional haptic feedback
- Multi-stage Mini App Docker image and Nginx API proxy
- Root Compose service for running the Mini App with Backend and PostgreSQL
- Environment-driven Backend CORS configuration for local Mini App development

### Changed

- Events and order endpoints no longer return placeholder responses.
- Payment creation now requires an existing payable order and derives amount/currency from it.
- Payment verification now updates the matching order before ticket fulfillment.
- Docker Compose now includes persistent PostgreSQL storage and the Mini App service.
- README and project-state documents distinguish implemented, tested, deployed, and verified work.
- Alembic uses environment-driven credentials and safely handles minimal logging configuration.

### Known limitations

- The executable MVP product flow is currently in memory and loses data on backend restart.
- Process-local state is not safe for multiple workers or production deployment.
- The Mini App production build and complete Docker runtime have not yet been executed and recorded.
- Telegram init-data authenticity is not yet validated.
- A passing current-head CI result is not yet recorded.
- Database-backed API integration, concurrent check-in, real payment, VPS, DNS, TLS, backup restore, rollback, and UAT remain unverified.
- Several relational-looking model columns remain without Foreign Key constraints.

## Historical Work Before Documentation Baseline

The repository contains earlier foundations for FastAPI, SQLAlchemy models, order/payment/ticket/check-in services, Telegram components, Docker Compose, Nginx, Certbot, deployment runbooks, and beta UAT planning. Historical work is not automatically considered tested, deployed, or verified. Refer to `docs/project/current-state.md` for current evidence levels.
