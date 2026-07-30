# Definition of Done

A task is complete only when every applicable requirement below is satisfied.

## Implementation

- The requested behavior exists in the repository.
- The implementation follows current architecture and coding conventions.
- Error handling and edge cases are addressed.
- No secrets or sensitive production data are committed.

## Verification

- Applicable unit, integration, build, lint, migration, and security checks were run.
- Results are recorded truthfully.
- Unexecuted checks and remaining uncertainty are explicitly disclosed.
- Environment-dependent work is not marked deployed or verified without evidence.

## Data and API

- Database changes include an executable migration and rollback consideration.
- API behavior and compatibility impacts are documented.
- Idempotency and concurrency are considered for payments, fulfillment, and check-in.

## Security

- Authentication and authorization impact is reviewed.
- Input validation, secret handling, logging, and abuse risks are considered.
- Payment callbacks or external webhooks are authenticated and replay-safe.

## Operations

- Deployment and configuration impact is documented.
- Health checks, observability, rollback, backup, and recovery are considered where relevant.

## Documentation

- A documentation impact assessment was performed.
- Affected canonical documents are updated.
- Current Project State remains accurate.
- Architecture decisions are recorded in ADRs when required.
- AI Handoff includes the exact next action and unresolved risks.
- `VERSION` and `CHANGELOG.md` are updated for releases.

## Continuity

A new developer or AI agent can understand what changed, why it changed, what was verified, what remains uncertain, and how to continue without access to previous chat history.
