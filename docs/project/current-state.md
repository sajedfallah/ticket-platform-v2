# Current Project State

- **Project:** Ticket Platform v2
- **Repository:** `sajedfallah/ticket-platform-v2`
- **Default branch:** `main`
- **Current version:** `0.2.0-prebeta`
- **Current phase:** Fast-track MVP execution and pre-beta verification
- **Current sprint:** First runnable product journey and local runtime readiness
- **Last reviewed commit:** `cf316d9dd46466cfcfd81f9811fd2fce0a217fad`
- **Last updated:** 2026-07-31

## Executive Status

The repository now contains a connected first product journey across Backend and Telegram Mini App: event discovery, quantity selection, validated order creation, mock payment, payment verification, ticket issuance, and QR display.

The Mini App is implemented as a responsive Persian RTL React/Vite application under `mini-app/`. It initializes the Telegram WebApp SDK when available and also supports browser-based local development. Nginx proxies `/api/` to the FastAPI service, and the root Docker Compose file can build the backend, PostgreSQL, and Mini App together.

This flow remains backed by process-local in-memory services. It is suitable for first boot and demos, but data is lost after backend restart and it is not safe for multiple workers or production use.

The project is **not yet a verified beta release** because no successful Mini App build, complete Docker runtime, current-head CI result, Telegram launch, or VPS deployment has been recorded.

## Capability Matrix

| Capability | Status | Evidence / limitation |
|---|---|---|
| FastAPI application bootstrap | IMPLEMENTED | Application and routers exist. |
| CORS configuration | IMPLEMENTED | Environment-driven origins with local Mini App defaults. Runtime unverified. |
| Event catalog | IMPLEMENTED | Seeded demo event plus list, detail, and create endpoints. In-memory only. |
| Order creation and lookup | IMPLEMENTED | Validates event, ticket type, quantity, capacity, and total. In-memory only. |
| Mock payment creation and verification | IMPLEMENTED | Payment uses server-side order amount and successful verification issues a ticket. |
| Ticket issuance, validation, and check-in | IMPLEMENTED | Ticket lookup, QR code value, active validation, and duplicate check-in protection exist. |
| Mini App purchase journey | IMPLEMENTED | React UI connects event → order → mock payment → ticket QR. Build/runtime not yet tested. |
| Telegram WebApp SDK bootstrap | IMPLEMENTED | Calls `ready()`, `expand()`, and optional haptic feedback. Telegram init-data authentication not implemented. |
| Mini App Docker image | IMPLEMENTED | Multi-stage Vite build and Nginx runtime exist. Build unverified. |
| Local Compose stack | IMPLEMENTED | Backend, PostgreSQL, and Mini App services are defined; runtime unverified. |
| First complete purchase journey test | IMPLEMENTED | Service-level flow test exists. Passing CI not recorded. |
| Database models and Alembic | IMPLEMENTED | Models, executable environment, and initial migration exist. |
| PostgreSQL verification workflow | IMPLEMENTED | Upgrade, drift check, downgrade, re-upgrade, and pytest configured. Result unverified. |
| Telegram bot | IMPLEMENTED | Foundation exists; real token and behavior unverified. |
| Admin panel | IMPLEMENTED | Foundation exists; event-management flow unverified. |
| VPS deployment | PLANNED | Runbook exists; not deployed. |

## Local First-Boot Target

```bash
docker compose up --build
```

Expected URLs after a successful build:

- Mini App: `http://localhost:8080`
- Backend API: `http://localhost:8000`
- Swagger: `http://localhost:8000/docs`

These URLs are expected from configuration and have not yet been runtime-verified.

## Current Priorities

1. Run `docker compose up --build` and fix the first runtime or build failure.
2. Verify the Mini App purchase flow in a browser.
3. Run `Backend Verification` and preserve the Summary/artifact.
4. Replace in-memory MVP state with SQLAlchemy repositories and transactions.
5. Add database-backed API integration tests and concurrent check-in protection.
6. Validate Telegram init data and connect the real BotFather Mini App URL.
7. Deploy a limited beta only after CI and runtime evidence are green.

## Known Issues and Technical Debt

- In-memory events, orders, payments, and tickets are lost on restart.
- The MVP service is process-local and unsuitable for multiple backend workers.
- Telegram init-data authenticity is not validated.
- A successful Node dependency install and Mini App production build have not been recorded.
- Database-backed API behavior and transaction isolation are not implemented end to end.
- Multiple relational-looking model columns still lack Foreign Keys.
- Authentication, authorization, and payment callback authenticity require audit.
- No passing current-head CI result is recorded.
- Docker, VPS, DNS, TLS, backup restore, rollback, and UAT remain unverified.

## Environment Status

| Environment | Status |
|---|---|
| GitHub Actions | VERIFICATION CONFIGURED; RESULT UNVERIFIED |
| Local Compose first boot | CONFIGURED; NOT RECORDED |
| Mini App connected flow | IMPLEMENTED; BUILD/RUNTIME UNVERIFIED |
| Telegram launch | NOT CONFIGURED |
| Beta VPS | NOT DEPLOYED |
| Production | NOT DEPLOYED |

## Next Recommended Action

Run `docker compose up --build` from the repository root. Open `http://localhost:8080`, complete the demo purchase, and record the first failing command or successful result. Do not mark the Mini App or Compose stack `TESTED` until this execution evidence exists.
