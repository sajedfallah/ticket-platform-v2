# Current Project State

- **Project:** Ticket Platform v2
- **Repository:** `sajedfallah/ticket-platform-v2`
- **Default branch:** `main`
- **Current version:** `0.2.0-prebeta`
- **Current phase:** Repository stabilization and pre-beta verification
- **Current sprint:** CI repair, test hardening, migration verification, and deployment readiness
- **Last reviewed commit:** `735e47be69928fc2af761d6d85b30f6302320f40`
- **Last updated:** 2026-07-30

## Executive Status

The repository contains a substantial event-ticketing foundation: FastAPI routes, SQLAlchemy models and services, order/payment/ticket flows, QR check-in protections, Docker production configuration, Nginx routing, Certbot TLS bootstrap, documentation governance, and a backend CI workflow.

The project is **not yet a verified beta release**. The backend CI workflow has now been corrected to use the real repository paths, and placeholder check-in coverage has been replaced with meaningful assertions. However, no passing current-head workflow result has yet been recorded, and deployment-dependent behavior remains unverified.

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
| Database migrations | DESIGNED | Migration documentation exists; complete executable migration chain is not verified. |
| Integration tests | IMPLEMENTED | Tests now cover idempotent issuance, single-use check-in, and unknown tickets. |
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

1. Obtain a passing GitHub Actions run for the corrected backend workflow.
2. Run the test suite from a clean environment and record exact output.
3. Verify imports, route contracts, and database behavior.
4. Establish and execute a clean Alembic migration chain.
5. Add Docker health checks and a fail-fast deployment script.
6. Review Telegram authentication, authorization, payment callbacks, and secret handling.
7. Deploy to the target VPS only after CI and migration evidence are green.
8. Execute and record limited beta UAT.

## Known Issues and Risks

- No passing current-head CI run has been recorded yet.
- The deployment system has been written but not executed on the target infrastructure.
- Certbot renewal may renew certificates without automatically reloading Nginx unless reload behavior is explicitly implemented and tested.
- Database migrations may be incomplete despite model definitions.
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

## Environment Status

| Environment | Status |
|---|---|
| Developer workstation | UNKNOWN |
| GitHub Actions | WORKFLOW REPAIRED; RESULT UNVERIFIED |
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

Trigger or observe the corrected `Backend Tests` workflow on `main`, retrieve the job result and logs, and fix only evidence-backed failures. If the workflow passes, update this file from `BLOCKED` to `TESTED` for the covered backend service behaviors.
