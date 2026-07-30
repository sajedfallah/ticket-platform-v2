# Project Roadmap

This roadmap is evidence-based. Status refers to repository and environment evidence, not prior chat claims.

## Phase 0 — Repository Memory and Governance

**Status:** IMPLEMENTED (baseline), ongoing maintenance required

- Canonical documentation index
- Truthful Current Project State
- Architecture overview
- AI context, bootstrap, master prompt, and handoff
- Status vocabulary and documentation precedence

Exit criteria:

- A new developer or AI can identify current state, risks, and next action without chat history.

## Phase 1 — Backend and Persistence Stabilization

**Status:** IMPLEMENTED / verification incomplete

- FastAPI bootstrap and routers
- SQLAlchemy models and services
- PostgreSQL session and transaction foundations
- Orders, payments, tickets, fulfillment, and check-in logic

Remaining exit criteria:

- Clean imports and application startup
- Complete migration chain from empty database
- Automated tests passing on current head
- No production path relying on unsafe in-memory state

## Phase 2 — Security and Contract Verification

**Status:** PLANNED

- Telegram `initData` verification
- Authentication and authorization model
- Admin and check-in operator access controls
- Payment callback signature verification and idempotency
- Rate limiting and abuse controls
- Secret-management review

Exit criteria:

- Security tests pass and threat-sensitive flows are documented.

## Phase 3 — Client Product Verification

**Status:** IMPLEMENTED foundation / NOT VERIFIED

- Telegram bot
- Telegram Mini App
- Admin panel

Remaining exit criteria:

- Build and test evidence
- Correct API configuration
- Telegram mobile flow validation
- Admin authorization validation
- Accessibility and RTL verification where applicable

## Phase 4 — Deployment Reliability

**Status:** IMPLEMENTED foundation / NOT DEPLOYED

- Docker Compose
- Nginx routing
- Certbot TLS bootstrap
- VPS and UAT runbooks

Remaining exit criteria:

- Docker health checks
- Fail-fast deployment
- Safe certificate renewal and Nginx reload
- Backup and restore test
- Rollback test
- Target VPS deployment evidence

## Phase 5 — Limited Beta

**Status:** PLANNED

- Real domain and TLS
- Telegram BotFather production configuration
- Sandbox or approved payment-provider integration
- One controlled event
- Limited test users and check-in operators
- Executed UAT report

Exit criteria:

- No unresolved critical defects
- Payment-to-ticket-to-check-in flow is VERIFIED
- Monitoring and incident response are usable

## Phase 6 — Public Launch

**Status:** PLANNED

- Legal and commercial readiness
- Organizer onboarding
- Refund and settlement operations
- Production support process
- Capacity and load validation
- Release and rollback discipline

## Immediate Priorities

1. Run backend CI/tests and repair failures.
2. Verify and complete Alembic migrations.
3. Audit authentication, authorization, payment callback, and idempotency.
4. Add health checks and deployment verification.
5. Build and test Mini App, bot, and admin panel.
6. Only then deploy to the target VPS and execute UAT.
