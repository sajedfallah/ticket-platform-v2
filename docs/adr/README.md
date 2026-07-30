# Architecture Decision Records

Use ADRs to record significant, durable technical decisions.

## When an ADR Is Required

Create an ADR when a change:

- changes system boundaries;
- selects or replaces a major technology;
- changes authentication or authorization;
- changes the database model or migration strategy;
- changes public API contracts;
- changes payment, ticket issuance, or check-in guarantees;
- changes deployment or security architecture;
- establishes a rule future contributors must follow;
- introduces an expensive or difficult-to-reverse tradeoff.

## Naming

```text
ADR-0001-short-title.md
ADR-0002-short-title.md
```

## Required Template

```markdown
# ADR-XXXX: Title

- Status: Proposed | Accepted | Superseded | Rejected | Deprecated
- Date: YYYY-MM-DD
- Decision owners:

## Context

## Decision

## Alternatives Considered

## Consequences

## Security Impact

## Data and Migration Impact

## Deployment Impact

## Affected Components

## Supersedes / Superseded By
```

## Rules

- Never silently rewrite an accepted decision.
- Correct minor errors in place; supersede changed decisions with a new ADR.
- Link relevant code, pull requests, issues, and documentation.
- Update architecture and current-state documents when an accepted ADR changes the active system.
