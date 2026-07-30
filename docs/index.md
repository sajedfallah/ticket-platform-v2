# Documentation Index

This directory is the canonical entry point for project knowledge.

## Canonical Documents

1. [Current project state](project/current-state.md) — the most important status document.
2. [Roadmap](project/roadmap.md) — priorities and phased delivery plan.
3. [Architecture overview](architecture/overview.md) — system boundaries and major components.
4. [AI context](ai/AI_CONTEXT.md) — stable context for AI contributors.
5. [AI bootstrap](ai/AI_BOOTSTRAP.md) — required repository-first workflow.
6. [AI master prompt](ai/AI_MASTER_PROMPT.md) — repository stewardship protocol.
7. [AI handoff](ai/AI_HANDOFF.md) — latest continuation state.

## Operational Documents

- [VPS deployment runbook](../launch/VPS_DEPLOYMENT_RUNBOOK.md)
- [Beta UAT checklist](../launch/BETA_UAT_CHECKLIST.md)
- [Monitoring foundation](../monitoring/README.md)
- [Database migrations](../backend/migrations/README.md)

## Source-of-Truth Precedence

When information conflicts, use this order:

1. Verified implementation and executable configuration
2. Accepted Architecture Decision Records
3. `docs/project/current-state.md`
4. Architecture and API documentation
5. Roadmap and sprint documents
6. README and onboarding summaries
7. Historical documents

## Documentation Rules

- Inspect before editing.
- Update canonical documents instead of creating duplicates.
- Distinguish `IMPLEMENTED` from `TESTED`, `DEPLOYED`, and `VERIFIED`.
- Record uncertainty and missing verification explicitly.
- Never commit secrets or real production credentials.
- Every behavior, architecture, security, database, or deployment change requires a documentation impact assessment.
