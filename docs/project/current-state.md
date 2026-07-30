# Current Project State

- **Project:** Ticket Platform v2
- **Repository:** `sajedfallah/ticket-platform-v2`
- **Default branch:** `main`
- **Current version:** `0.2.0-prebeta`
- **Current phase:** Fast-track MVP execution and pre-beta verification
- **Current sprint:** First executable purchase journey, CI verification, and runtime readiness
- **Last reviewed commit:** `26097bd27bb778c5fcac2cdb7b3c9e1bcc711ba1`
- **Last updated:** 2026-07-31

## Executive Status

The backend now contains an executable first product journey: a seeded published event, event listing/detail/creation, validated order creation, mock payment creation tied to the real order amount, payment verification, ticket issuance, QR-code ticket lookup, and single-use check-in.

This flow is currently backed by an in-memory MVP service. It is suitable for first boot, Swagger testing, Mini App integration, and product demonstrations, but data is lost when the backend process restarts. PostgreSQL repositories and transaction-backed concurrency remain required before beta deployment.

The project is **not yet a verified beta release** because no successful current-head GitHub Actions run, Docker runtime test, Telegram integration test, or VPS deployment has been recorded.

## Capability Matrix

| Capability | Status | Evidence / limitation |
|---|---|---|
| FastAPI application bootstrap | IMPLEMENTED | Application and routers exist. |
| Health route | IMPLEMENTED | Production behavior not verified. |
| Event catalog | IMPLEMENTED | Seeded demo event plus list, detail, and create endpoints. In-memory only. |
| Order creation and lookup | IMPLEMENTED | Validates event, ticket type, quantity, capacity, and calculates total. In-memory only. |
| Mock payment creation | IMPLEMENTED | Uses order amount/currency and rejects unknown or non-payable orders. |
| Payment verification | IMPLEMENTED | Updates order status and issues a ticket after successful mock payment. |
| Ticket issuance and lookup | IMPLEMENTED | Idempotent ticket issuance by order. In-memory only. |
| QR validation and check-in | IMPLEMENTED | Active validation and duplicate check-in protection exist. |
| First complete purchase journey test | IMPLEMENTED | Covers event → order → payment → ticket → check-in at service level. Passing CI not recorded. |
| Database models and Alembic | IMPLEMENTED | Models, executable environment, and initial migration exist. |
| PostgreSQL migration verification workflow | IMPLEMENTED | Upgrade, drift check, downgrade, re-upgrade, and pytest are configured. Result unverified. |
| GitHub verification report | IMPLEMENTED | Summary and retained first-failure artifact are configured. |
| Telegram bot | IMPLEMENTED | Foundation exists; real token and behavior unverified. |
| Telegram Mini App | IMPLEMENTED | Build foundation exists; connection to new API flow remains next. |
| Admin panel | IMPLEMENTED | Build foundation exists; real event-management flow unverified. |
| Docker Compose and Nginx | IMPLEMENTED | Runtime health and target deployment remain unverified. |
| VPS deployment | PLANNED | Runbook exists; not deployed. |

## Executable MVP API Flow

1. `GET /api/events`
2. `GET /api/events/{event_id}`
3. `POST /api/events`
4. `POST /api/orders`
5. `GET /api/orders/{order_id}`
6. `POST /api/payments/create`
7. `POST /api/payments/verify`
8. `GET /api/tickets/order/{order_id}`
9. `POST /api/tickets/validate`
10. `POST /api/tickets/check-in`

## Current Priorities

1. Connect the Mini App to the executable event/order/payment/ticket endpoints.
2. Run `Backend Verification` and fix the first evidence-backed failure.
3. Replace in-memory MVP state with SQLAlchemy repositories and transactions.
4. Add database-backed API integration tests and concurrent check-in protection.
5. Add Docker health checks and fail-fast deployment behavior.
6. Configure Telegram authentication and real BotFather settings.
7. Deploy a limited beta only after CI and runtime evidence are green.

## Known Issues and Technical Debt

- In-memory events, orders, payments, and tickets are lost on restart.
- The MVP service is process-local and unsuitable for multiple backend workers.
- Database-backed API behavior and transaction isolation are not implemented end to end.
- Multiple relational-looking model columns still lack Foreign Keys.
- Authentication, authorization, Telegram init-data validation, and payment callback authenticity require audit.
- No passing current-head CI result is recorded.
- Docker, VPS, DNS, TLS issuance, backup restore, rollback, and UAT remain unverified.

## Environment Status

| Environment | Status |
|---|---|
| GitHub Actions | VERIFICATION CONFIGURED; RESULT UNVERIFIED |
| Local backend first boot | NOT RECORDED |
| Mini App connected flow | NOT IMPLEMENTED |
| Beta VPS | NOT DEPLOYED |
| Production | NOT DEPLOYED |

## Next Recommended Action

Connect the Mini App event list and purchase action to the new executable API flow. In parallel, manually dispatch `Backend Verification` on the latest `main` head and preserve the Summary or artifact as evidence.
