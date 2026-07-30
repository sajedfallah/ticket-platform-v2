# Current Project State

- **Project:** Ticket Platform v2
- **Repository:** `sajedfallah/ticket-platform-v2`
- **Default branch:** `main`
- **Current version:** `0.2.0-prebeta`
- **Current phase:** Repository stabilization and pre-beta verification
- **Current sprint:** CI, migration lifecycle, database verification, and deployment readiness
- **Last reviewed commit:** `52f8f14c51f0676fdaa8fc09d6394d4100c19d09`
- **Last updated:** 2026-07-30

## Executive Status

The repository contains a substantial event-ticketing foundation: FastAPI routes, SQLAlchemy models and services, order/payment/ticket flows, QR check-in protections, Docker production configuration, Nginx routing, Certbot TLS bootstrap, repository governance, backend tests, an executable Alembic environment, an initial migration revision, and a GitHub Actions verification workflow backed by PostgreSQL 16.

The project is **not yet a verified beta release**. The workflow now defines clean-database upgrade, schema-drift checking, downgrade to base, re-upgrade, compilation, and backend tests. However, no successful run result or job log has yet been recorded, so these capabilities remain implemented rather than tested.

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
| Initial migration revision | IMPLEMENTED | `20260730_0001_initial_schema.py` mirrors current model declarations. |
| PostgreSQL migration verification workflow | IMPLEMENTED | CI provisions PostgreSQL 16 and runs upgrade, drift check, downgrade, and re-upgrade. No passing result recorded. |
| Clean migration lifecycle | BLOCKED | Workflow exists, but successful execution evidence is missing. |
| Integration tests | IMPLEMENTED | Tests cover idempotent issuance, single-use check-in, and unknown tickets. |
| Current-head automated tests | BLOCKED | Test code exists, but no passing current-head execution evidence has been recorded. |
| GitHub Actions backend verification | IMPLEMENTED | Workflow now includes PostgreSQL migration lifecycle and backend tests; result unverified. |
| Telegram bot | IMPLEMENTED | Container/service foundation exists; real token and behavior not verified. |
| Telegram Mini App | IMPLEMENTED | Build/service foundation exists; product flow and production rendering not verified. |
| Admin panel | IMPLEMENTED | Build/service foundation exists; authorization and production rendering not verified. |
| Production Docker Compose | IMPLEMENTED | Services and volumes are defined; application health checks remain incomplete. |
| Nginx routing | IMPLEMENTED | `/api`, `/app`, `/admin`, and health routing exist. |
| TLS bootstrap | IMPLEMENTED | Certbot bootstrap and HTTPS template exist; real issuance not verified. |
| VPS deployment | PLANNED | Runbook exists; no target VPS deployment evidence. |
| Real DNS and domain | BLOCKED | Requires owner-provided domain and DNS changes. |
| Real payment | BLOCKED | Requires provider selection, credentials, and sandbox verification. |
| Beta UAT | PLANNED | Checklist exists; no executed test report. |

## Current Priorities

1. Obtain and inspect a successful or failing run of `Backend Verification` on the current head.
2. Fix only evidence-backed workflow, migration, or test failures.
3. Record exact PostgreSQL upgrade, downgrade, re-upgrade, drift-check, and pytest output.
4. Add Docker health checks and a fail-fast deployment script after CI is green.
5. Reconcile in-memory and database-backed order/payment/ticket flows.
6. Review Telegram authentication, authorization, payment callbacks, and secret handling.
7. Deploy to the target VPS only after CI and migration evidence are green.
8. Execute and record limited beta UAT.

## Known Issues and Risks

- No passing current-head CI run has been recorded yet.
- The PostgreSQL verification workflow is implemented but has not produced recorded evidence.
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
- Test isolation does not yet cover database-backed API behavior or concurrent check-in.
- The Alembic model import list must remain synchronized with `backend/app/models`.
- Foreign Key coverage is incomplete across orders, payments, ticket types, order items, discounts, and check-ins.

## Environment Status

| Environment | Status |
|---|---|
| Developer workstation | UNKNOWN |
| GitHub Actions | POSTGRESQL VERIFICATION WORKFLOW IMPLEMENTED; RESULT UNVERIFIED |
| Ephemeral PostgreSQL 16 CI service | CONFIGURED; EXECUTION UNVERIFIED |
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

Observe the `Backend Verification` workflow created by commit `52f8f14c51f0676fdaa8fc09d6394d4100c19d09`. Retrieve its job result and logs. If it fails, repair only the observed root cause. If all migration and test steps pass, mark the covered migration lifecycle and backend service behaviors as `TESTED` and preserve the run URL or identifiers as evidence.
