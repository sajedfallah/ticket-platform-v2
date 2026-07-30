# Current Project State

- **Project:** Ticket Platform v2
- **Repository:** `sajedfallah/ticket-platform-v2`
- **Default branch:** `main`
- **Current version:** `0.2.0-prebeta`
- **Current phase:** Repository stabilization and pre-beta verification
- **Current sprint:** CI, migration lifecycle, database verification, and deployment readiness
- **Last reviewed commit:** `c1e32e7bd240000f3f498ae135e4dbdd46364e53`
- **Last updated:** 2026-07-30

## Executive Status

The repository contains a substantial event-ticketing foundation: FastAPI routes, SQLAlchemy models and services, order/payment/ticket flows, QR check-in protections, Docker production configuration, Nginx routing, Certbot TLS bootstrap, repository governance, backend tests, an executable Alembic environment, an initial migration revision, and a PostgreSQL-backed GitHub Actions verification workflow.

The project is **not yet a verified beta release**. Verification is now centralized in `backend/scripts/verify_backend.sh`, which records each successful step and the first failed step in a Markdown report. GitHub Actions publishes that report to the run summary and retains it as an artifact. No successful workflow result has yet been recorded, so migration and test capabilities remain implemented rather than tested.

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
| Alembic runtime environment | IMPLEMENTED | Online/offline execution, model registration, environment-driven URL handling, and safe optional logging configuration exist. |
| Initial migration revision | IMPLEMENTED | `20260730_0001_initial_schema.py` mirrors current model declarations. |
| PostgreSQL migration verification workflow | IMPLEMENTED | CI provisions PostgreSQL 16 and invokes the reusable verification script. No passing result recorded. |
| Verification report and artifact | IMPLEMENTED | Each run produces a step summary and retained Markdown artifact, including the first failed step. |
| Clean migration lifecycle | BLOCKED | Workflow exists, but successful execution evidence is missing. |
| Integration tests | IMPLEMENTED | Tests cover idempotent issuance, single-use check-in, and unknown tickets. |
| Current-head automated tests | BLOCKED | Test code exists, but no passing current-head execution evidence has been recorded. |
| GitHub Actions backend verification | IMPLEMENTED | Workflow includes PostgreSQL migration lifecycle, schema drift check, and backend tests; result unverified. |
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

1. Run `Backend Verification` on the current `main` head.
2. Inspect the generated Summary and `backend-verification-<sha>` artifact.
3. Fix only the first evidence-backed failing step.
4. Record exact PostgreSQL upgrade, drift-check, downgrade, re-upgrade, and pytest evidence.
5. Add Docker health checks and a fail-fast deployment script after CI is green.
6. Reconcile in-memory and database-backed order/payment/ticket flows.
7. Review Telegram authentication, authorization, payment callbacks, and secret handling.
8. Deploy to the target VPS only after CI and migration evidence are green.
9. Execute and record limited beta UAT.

## Known Issues and Risks

- No passing current-head CI run has been recorded yet.
- The PostgreSQL verification workflow is implemented but has not produced recorded success evidence.
- The connector view available during this audit did not expose push-based workflow runs.
- The audit execution environment could not resolve `github.com`, so an independent clone-and-run verification could not be completed.
- Several relational-looking columns are plain integers without Foreign Key constraints because current models do not declare those constraints.
- The deployment system has been written but not executed on target infrastructure.
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
| GitHub Actions | POSTGRESQL VERIFICATION + REPORTING IMPLEMENTED; RESULT UNVERIFIED |
| Ephemeral PostgreSQL 16 CI service | CONFIGURED; EXECUTION UNVERIFIED |
| Audit execution environment | NETWORK BLOCKED FOR GITHUB CLONE |
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

Manually dispatch `Backend Verification` on the latest `main` head. Open the run Summary or download the `backend-verification-<sha>` artifact, then repair only the first failed step. If every recorded step passes, mark the covered migration lifecycle and backend service behaviors as `TESTED` and preserve the run URL and commit SHA as evidence.
