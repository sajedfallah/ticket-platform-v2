# Documentation Rules

## Purpose

Documentation is part of the product and must remain aligned with the repository.

## Canonical Documents

- `README.md` — concise entry point
- `docs/index.md` — documentation map and precedence
- `docs/project/current-state.md` — exact active status
- `docs/project/roadmap.md` — delivery sequence and priorities
- `docs/architecture/overview.md` — active architecture
- `docs/ai/AI_CONTEXT.md` — stable AI context
- `docs/ai/AI_HANDOFF.md` — latest continuation state
- `CHANGELOG.md` and `VERSION` — release history and version

## Documentation Impact Assessment

For every material change, evaluate impact on:

- product behavior;
- architecture;
- domain or data model;
- API contracts;
- security;
- deployment and operations;
- tests and Definition of Done;
- roadmap and current state;
- changelog and version;
- AI context and handoff.

Update only affected canonical documents. Do not create duplicate status or architecture files.

## Evidence Rules

- A code file proves only `IMPLEMENTED` status.
- A test file does not prove `TESTED`; passing execution evidence is required.
- Deployment configuration does not prove `DEPLOYED`.
- A successful deployment does not prove `VERIFIED`; behavior must be checked.
- Uncertainty must be recorded, not hidden.

## Change Rules

- Every architecture decision requires an ADR when it meets the ADR threshold.
- Every sprint or material work session must leave Current Project State and AI Handoff accurate.
- Every release updates `VERSION`, `CHANGELOG.md`, current state, and deployment/migration instructions when affected.
- Historical documents must be marked and must not override current canonical documents.

## Security

Never document real secrets, tokens, credentials, private keys, personal data, or production `.env` values.

## Review Checklist

Before merging a documentation change:

- Links and paths are correct.
- Claims match repository evidence.
- Status terms are used consistently.
- No duplicate source of truth was created.
- Dates, version, phase, and next action are accurate.
- The next contributor can continue without chat history.
