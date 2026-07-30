# AI Context

## Project

Ticket Platform v2 is a pre-beta event-ticketing platform with Telegram bot and Mini App access, an admin surface, a FastAPI backend, PostgreSQL persistence, Redis, Nginx, Docker Compose, and a Certbot TLS bootstrap.

## Repository Truth

- Repository: `sajedfallah/ticket-platform-v2`
- Default branch: `main`
- Canonical status: `docs/project/current-state.md`
- Canonical architecture: `docs/architecture/overview.md`
- Canonical roadmap: `docs/project/roadmap.md`

## Current Reality

Several backend and deployment components are `IMPLEMENTED`, but the full system is not yet `TESTED`, `DEPLOYED`, or `VERIFIED` as a beta release.

Do not repeat historical phase-completion claims without repository evidence.

## Status Vocabulary

Use only:

- `PLANNED`
- `DESIGNED`
- `IMPLEMENTED`
- `TESTED`
- `DEPLOYED`
- `VERIFIED`
- `BLOCKED`
- `DEPRECATED`

## Stable Architectural Rules

1. PostgreSQL is the intended production system of record.
2. Payment integration must remain behind a provider abstraction.
3. Ticket issuance follows verified, idempotent payment completion.
4. Duplicate check-in protection is mandatory.
5. Secrets and production `.env` files must never be committed.
6. Do not claim deployment merely because deployment configuration exists.
7. Significant architecture changes require an ADR.
8. Every task requires a documentation impact assessment.

## Immediate Work Order

1. Run and repair backend tests and CI.
2. Reconcile in-memory and database-backed code paths.
3. Verify a complete Alembic migration path.
4. Audit authentication, authorization, payment callbacks, and idempotency.
5. Add Docker health checks and fail-fast deployment behavior.
6. Verify Telegram bot, Mini App, and admin panel builds.
7. Deploy only after local and CI evidence is green.

## Known Risks

- Current-head CI result is not recorded.
- Real payment-provider behavior is not verified.
- Telegram authentication is not proven.
- VPS, DNS, TLS, restore, rollback, and UAT are not executed.
- Certbot renewal and Nginx reload behavior require verification.
- Database migration completeness is unknown.

## Mandatory Contributor Behavior

Inspect files before editing. Prefer evidence over assumptions. Never invent tests, commits, deployments, or capabilities. Update `current-state.md` and `AI_HANDOFF.md` whenever project state materially changes.
