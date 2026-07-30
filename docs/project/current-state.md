# Current Project State

- **Project:** Ticket Platform v2
- **Repository:** `sajedfallah/ticket-platform-v2`
- **Default branch:** `main`
- **Current version:** `0.2.0-prebeta`
- **Current phase:** Repository stabilization and pre-beta verification
- **Current sprint:** Documentation baseline, deployment hardening, and evidence collection
- **Last reviewed commit before this baseline:** `fc8e661968b7f4375e1d9a7ae3a8c247191f1c04`
- **Last updated:** 2026-07-30

## Executive Status

The repository contains a working foundation for an event-ticketing system, including backend routes, persistence models, payment/ticket fulfillment code, QR check-in protections, an integration-test foundation, Docker production configuration, Nginx routing, and Certbot TLS bootstrap.

The project is **not yet a verified beta release**. No evidence has been recorded that the current head passes all tests, migrates a clean production database, deploys successfully to the target VPS, connects to a real Telegram bot, completes a real provider payment, or passes end-to-end mobile UAT.

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
| QR validation and duplicate check-in protection | IMPLEMENTED | Route logic exists; concurrency behavior not yet verified against PostgreSQL. |
| Database models/session/transactions | IMPLEMENTED | SQLAlchemy foundations exist. |
| Database migrations | DESIGNED | Migration documentation exists; complete executable migration chain is not verified. |
| Integration-test foundation | IMPLEMENTED | Payment-ticket-check-in test exists. |
| Current-head automated tests | BLOCKED | No passing result has been recorded during this audit. |
| GitHub Actions backend CI | IMPLEMENTED | Workflow exists; current run status has not been verified. |
| Telegram bot | IMPLEMENTED | Container/service foundation exists; real token and behavior not verified. |
| Telegram Mini App | IMPLEMENTED | Build/service foundation exists; product flow and production rendering not verified. |
| Admin panel | IMPLEMENTED | Build/service foundation exists; authorization and production rendering not verified. |
| Production Docker Compose | IMPLEMENTED | Services and volumes are defined. |
| Nginx routing | IMPLEMENTED | `/api`, `/app`, `/admin`, and health routing exist. |
| TLS bootstrap | IMPLEMENTED | Certbot bootstrap and HTTPS template exist; real issuance not verified. |
| VPS deployment | PLANNED | Runbook exists; no target VPS deployment evidence. |
| Real DNS and domain | BLOCKED | Requires owner-provided domain and DNS changes. |
| Real payment | BLOCKED | Requires provider selection, credentials, and sandbox verification. |
| Beta UAT | PLANNED | Checklist exists; no executed test report. |

## Current Priorities

1. Complete repository documentation baseline and remove contradictory claims.
2. Run and repair backend tests and CI.
3. Verify imports, route contracts, and database behavior from a clean environment.
4. Establish an executable Alembic migration chain.
5. Add Docker health checks and a fail-fast deployment script.
6. Review Telegram authentication, authorization, payment callbacks, and secret handling.
7. Deploy to the target VPS only after local/CI evidence is green.
8. Execute and record limited beta UAT.

## Known Issues and Risks

- README and prior phase summaries previously overstated completion relative to verification evidence.
- The deployment system has been written but not executed on the target infrastructure.
- Certbot renewal may renew certificates without automatically reloading Nginx unless reload behavior is explicitly implemented and tested.
- Database migrations may be incomplete despite model definitions.
- Some API/service flows may combine in-memory and database-backed behavior; this requires code-level reconciliation.
- Authentication and authorization coverage has not been proven.
- Payment callback authenticity and idempotency require security verification.
- Check-in duplicate protection must be tested under concurrent requests.
- Secrets must remain outside Git and be rotated if previously exposed.

## Technical Debt

- Canonical API documentation is missing.
- Canonical domain and database diagrams are missing.
- ADR history is missing for major technology and deployment decisions.
- Definition of Done, branch strategy, release process, and contribution standards are not yet fully documented.
- Frontend and bot tests are not evidenced.
- Observability documentation exists, but operational metrics and alerting are not verified.

## Environment Status

| Environment | Status |
|---|---|
| Developer workstation | UNKNOWN |
| GitHub Actions | UNKNOWN |
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

Audit and run the backend test suite and GitHub Actions workflow. Fix failures before adding new features or deploying to a VPS.
