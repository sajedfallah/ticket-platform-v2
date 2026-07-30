# AI Handoff

## Objective

Stabilize the repository, establish truthful project memory, and verify the backend before any new feature or VPS deployment work.

## Work Completed

- Replaced the outdated README with a repository-first and evidence-based entry point.
- Added canonical documentation, current-state, roadmap, architecture, AI context, bootstrap, master prompt, and handoff files.
- Audited the backend CI workflow and found that it ran from the repository root while dependencies live under `backend/`.
- Added `backend/requirements-dev.txt` with explicit test dependencies.
- Corrected `.github/workflows/backend-test.yml` to use the backend working directory, correct dependency paths, backend compilation, and explicit `PYTHONPATH`.
- Replaced a placeholder `assert True` integration gate with real assertions for:
  - idempotent ticket issuance;
  - single-use ticket check-in;
  - rejection of unknown ticket codes.
- Updated Current Project State and CHANGELOG with the new evidence and remaining limitations.

## Files Changed or Added

- `README.md`
- `VERSION`
- `CHANGELOG.md`
- `.github/workflows/backend-test.yml`
- `backend/requirements-dev.txt`
- `tests/integration/test_payment_ticket_checkin_flow.py`
- `docs/index.md`
- `docs/project/current-state.md`
- `docs/project/roadmap.md`
- `docs/architecture/overview.md`
- `docs/development/documentation-rules.md`
- `docs/development/definition-of-done.md`
- `docs/adr/README.md`
- `docs/ai/AI_CONTEXT.md`
- `docs/ai/AI_BOOTSTRAP.md`
- `docs/ai/AI_MASTER_PROMPT.md`
- `docs/ai/AI_HANDOFF.md`

## Key Findings

- The repository is pre-beta, not a verified beta release.
- The original CI workflow referenced `requirements.txt` and `pytest` from the repository root, but the dependency file is inside `backend/` and `pytest` was not declared.
- The existing check-in test contained a placeholder assertion and did not validate behavior.
- Backend, persistence, payment/ticket/check-in, Docker, Nginx, and Certbot foundations exist.
- Current-head passing CI, complete migrations, real payment, Telegram production configuration, VPS deployment, backup restore, rollback, and UAT remain unverified.

## Verification Performed

- Inspected repository metadata, commit history, backend workflow, backend requirements, application bootstrap, fulfillment service, and integration tests through the GitHub connector.
- Confirmed no pull-request-triggered workflow run was returned for the inspected commits.
- Corrected evidence-backed CI and test defects.

## Tests Not Yet Executed or Proven Passing

- Corrected GitHub Actions backend workflow on current head
- Local clean-environment backend test run
- Clean-database Alembic migration
- Database-backed API integration tests
- Concurrent check-in protection
- Docker Compose build and health checks
- Telegram bot and Mini App builds
- Admin panel build
- Real payment-provider flow
- VPS/DNS/TLS deployment
- Backup restore and rollback
- End-to-end UAT

## Current Blockers

- No passing current-head CI result has been recorded.
- No complete executable migration-chain evidence.
- No target VPS or domain execution evidence.
- No real Telegram or payment-provider configuration.
- Authentication and authorization require audit.

## Exact Next Action

Observe or trigger the corrected `Backend Tests` workflow on `main`. Retrieve its jobs and logs. If it fails, fix only the observed root cause. If it passes, update `docs/project/current-state.md` to mark the covered backend service behavior as `TESTED`, then proceed to clean-database migration verification.

## Required Human Inputs for Later Deployment

- Domain and DNS access
- VPS IP, OS, and SSH user
- BotFather configuration
- Payment provider and sandbox credentials
- Business rules for refunds, settlements, and organizer onboarding

Never place secrets in GitHub files, issues, commits, or chat.
