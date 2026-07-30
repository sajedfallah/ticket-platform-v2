# Current Project State

- **Project:** Ticket Platform v2
- **Repository:** `sajedfallah/ticket-platform-v2`
- **Default branch:** `main`
- **Current version:** `0.2.0-prebeta`
- **Current phase:** Repository stabilization and pre-beta verification
- **Current sprint:** CI repair, test hardening, migration verification, and deployment readiness
- **Last reviewed commit:** `8352ceb468b6c095abefbf771b57ab9a519fb247`
- **Last updated:** 2026-07-30

## Executive Status

The repository contains a substantial event-ticketing foundation: FastAPI routes, SQLAlchemy models and services, order/payment/ticket flows, QR check-in protections, Docker production configuration, Nginx routing, Certbot TLS bootstrap, documentation governance, a backend CI workflow, an executable Alembic environment, and a reviewed initial migration revision matching the current model declarations.

The project is **not yet a verified beta release**. The migration revision is implemented but has not been executed against a clean PostgreSQL database, downgraded, upgraded again, or compared with a fresh autogenerate result. No passing current-head CI result has been recorded.

## Capability Matrix

| Capability | Status | Evidence / limitation |
|---|---|---|
| FastAPI application bootstrap | IMPLEMENTED | Application and router registration exist. |
| Health route | IMPLEMENTED | Backend health router is registered; production behavior not yet verified. |
| Event CRUD foundation | IMPLEMENTED | Router exists; authorization and production persistence require verification. |
| Order lifecycle | IMPLEMENTED | Order model/service lifecycle states exist. |
| Payment provider abstraction | IMPLEMENTED | Provider integration foundation exists; no real provider verified. |
| Payment verification flow | IMPLEMENTED | API and fulfillment wiring exist; security/idempotency need full review. |
| Ticket issuance | IMPLEMENTED | Fulfillment and ticket services exist. |
| QR validation and duplicate check-in protection | IMPLEMENTED | Service and route logic exist; concurrent PostgreSQL behavior is not verified. |
| Database models/session/transactions | IMPLEMENTED | SQLAlchemy foundations exist. |
| Alembic runtime environment | IMPLEMENTED | Online/offline execution, model registration, logging, and environment-driven URL handling exist. |
| Initial migration revision | IMPLEMENTED | `20260730_0001_initial_schema.py` mirrors the current model declarations; database execution is unverified. |
| Clean migration lifecycle | BLOCKED | Upgrade, downgrade, re-upgrade, and autogenerate-diff evidence are not recorded. |
| Integration tests | IMPLEMENTED | Tests cover idempotent issuance, single-use check-in, and unknown tickets. |
| Current-head automated tests | BLOCKED | Test code exists, but no passing current-head execution evidence has been recorded. |
| GitHub Actions backend CI | IMPLEMENTED | Workflow paths and test dependencies were corrected; a passing run is not yet verified. |
| Telegram bot | IMPLEMENTED | Container/service foundation exists; real token and behavior not verified. |
| Telegram Mini App | IMPLEMENTED | Build/service foundation exists; product flow and production rendering not verified. |
| Admin panel | IMPLEMENTED | Build/service foundation exists; authorization and production rendering not verified. |
| Production Docker Compose | IMPLEMENTED | Services and volumes are defined; health checks remain incomplete. |
| Nginx routing | IMPLEMENTED | `/api`, `/app`, `/admin`, and health routing exist. |
| TLS bootstrap | IMPLEMENTED | Certbot bootstrap and HTTPS template exist; real issuance not verified. |
| VPS deployment | PLANNED | Runbook exists; no target VPS deployment evidence. |
| Real DNS and domain | BLOCKED | Requires owner-provided domain and DNS changes. |
| Real payment | BLOCKED | Requires provider selection, credentials, and sandbox verification. |
| Beta UAT | PLANNED | Checklist exists; no executed test report. |

## Current Priorities

1. Execute the reviewed initial migration against a clean PostgreSQL database.
2. Verify `alembic downgrade base` and `alembic upgrade head`.
3. Run `alembic revision --autogenerate` after upgrade and confirm there is no unintended schema drift.
4. Obtain a passing GitHub Actions run for the corrected backend workflow.
5. Run the backend test suite from a clean environment and record exact output.
6. Add Docker health checks and a fail-fast deployment script.
7. Review Telegram authentication, authorization, payment callbacks, and secret handling.
8. Deploy to the target VPS only after CI and migration evidence are green.
9. Execute and record limited beta UAT.

## Known Issues and Risks

- No passing current-head CI run has been recorded yet.
- The initial migration revision has not been executed on PostgreSQL.
- Several relational-looking columns are plain integers without Foreign Key constraints because the current models do not declare those constraints.
- The deployment system has been written but not executed on the target infrastructure.
- Certbot renewal may renew certificates without automatically reloading Nginx unless reload behavior is explicitly implemented and tested.
- Some API/service flows may combine in-memory and database-backed behavior; this requires reconciliation.
- Authentication and authorization coverage has not been proven.
- Payment callback authenticity and idempotency require security verification.
- Check-in duplicate protection must be tested under concurrent database-backed requests.
- Secrets must remain outside Git and be rotated if previously exposed.

## Technical Debt

- Canonical API documentation is missing.
- Canonical domain and database diagrams are missing.
- ADR history is missing for major technology and deployment decisions.
- Branch strategy and release process are not yet fully documented.
- Frontend and bot tests are not evidenced.
- Observability documentation exists, but operational metrics and alerting are not verified.
- Test isolation is currently service-level and does not yet cover real PostgreSQL transactions.
- The Alembic model import list must remain synchronized with `backend/app/models`.
- Foreign Key coverage is incomplete across orders, payments, ticket types, order items, discounts, and check-ins.

## Environment Status

| Environment | Status |
|---|---|
| Developer workstation | UNKNOWN |
| GitHub Actions | WORKFLOW REPAIRED; RESULT UNVERIFIED |
| Clean PostgreSQL migration environment | NOT EXECUTED |
| Beta VPS | NOT DEPLOYED |
| Production | NOT DEPLOYED |

## Required Human Inputs

- Target domain and DNS access
- VPS IP, operating system, and SSH user
- Telegram bot configuration through BotFather
- Payment provider choice and sandbox credentials
- Legal/business rules for refunds, organizer onboarding, and settlement

Do not place passwords, bot tokens, private keys, payment secrets, or production `.env` content in documentation, issues, commits, or chat.

## Next Recommended Action

Run the reviewed initial migration in a disposable PostgreSQL environment, verify upgrade/downgrade/re-upgrade behavior, run a no-drift autogenerate comparison, and record exact evidence. In parallel, observe the corrected `Backend Tests` workflow and record its result before upgrading any capability to `TESTED`.
