# Ticket Platform v2

Ticket Platform v2 is an event-ticketing platform intended to support event discovery, ordering, payment verification, ticket issuance, QR validation, Telegram access, administration, and production deployment.

> **Repository status:** active foundation / pre-beta. Code exists for several backend and deployment capabilities, but the system has not yet been verified on the target VPS with a real domain, Telegram bot, or payment provider.

## Start Here

- [Documentation index](docs/index.md)
- [Current project state](docs/project/current-state.md)
- [Architecture overview](docs/architecture/overview.md)
- [Roadmap](docs/project/roadmap.md)
- [AI bootstrap guide](docs/ai/AI_BOOTSTRAP.md)
- [AI context](docs/ai/AI_CONTEXT.md)
- [AI handoff](docs/ai/AI_HANDOFF.md)
- [VPS deployment runbook](launch/VPS_DEPLOYMENT_RUNBOOK.md)
- [Beta UAT checklist](launch/BETA_UAT_CHECKLIST.md)

## Technology Baseline

- Backend: FastAPI, SQLAlchemy, Alembic, PostgreSQL
- Cache/runtime dependency: Redis
- Interfaces: Telegram bot, Telegram Mini App, admin panel
- Edge: Nginx
- Packaging and operations: Docker Compose, GitHub Actions
- TLS: Let's Encrypt / Certbot bootstrap

## Verified Repository Facts

- FastAPI application and routers exist.
- Models and services exist for orders, payments, tickets, fulfillment, and check-in foundations.
- A payment-to-ticket integration test exists in the repository.
- A backend CI workflow exists.
- Production Docker Compose, Nginx, Certbot, and deployment runbooks exist.

## Not Yet Verified

- Passing CI on the current head
- Full database migration path from an empty production database
- Real payment-provider integration
- Telegram authentication and BotFather production configuration
- Mini App and admin-panel production behavior
- VPS deployment, DNS, TLS issuance, backup restore, and end-to-end UAT

## Status Vocabulary

Use only these states in project documentation:

`PLANNED`, `DESIGNED`, `IMPLEMENTED`, `TESTED`, `DEPLOYED`, `VERIFIED`, `BLOCKED`, `DEPRECATED`.

Do not use vague completion claims. A documented design is not an implementation, and an implementation is not a verified deployment.

## Repository Rule

The repository is the project memory and single source of truth. Architecture, behavior, status, and operational decisions must be discoverable here without relying on previous chat history.
