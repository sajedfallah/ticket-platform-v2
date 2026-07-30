# AI Bootstrap Guide

Follow this sequence before changing the repository.

## 1. Orient

Read, in order:

1. `README.md`
2. `docs/index.md`
3. `docs/project/current-state.md`
4. `docs/architecture/overview.md`
5. `docs/project/roadmap.md`
6. `docs/ai/AI_CONTEXT.md`
7. `docs/ai/AI_HANDOFF.md`

## 2. Inspect Before Editing

- Confirm the default branch and latest commit.
- Read every source and configuration file directly affected by the task.
- Search for existing implementations and documentation before creating new files.
- Identify whether the requested work is planning, design, implementation, testing, deployment, or verification.

## 3. State the Evidence Level

Use the repository status vocabulary:

`PLANNED`, `DESIGNED`, `IMPLEMENTED`, `TESTED`, `DEPLOYED`, `VERIFIED`, `BLOCKED`, `DEPRECATED`.

Never promote a capability to a higher status without evidence.

## 4. Make a Coherent Change

- Preserve existing architecture unless a documented decision justifies change.
- Prefer small, reviewable changes.
- Do not mix unrelated refactoring with feature work.
- Never commit secrets, tokens, passwords, private keys, or real production environment files.

## 5. Validate

Run all applicable checks. Record exactly what ran and the result.

If a test cannot run, record:

- why it could not run;
- what remains uncertain;
- the exact next verification command or action.

## 6. Documentation Impact Assessment

Evaluate whether the change affects:

- README
- Current Project State
- Roadmap
- Architecture
- API or database documentation
- Security or deployment documentation
- ADRs
- Known issues or technical debt
- Changelog or version
- AI Context and AI Handoff

Update only affected canonical documents.

## 7. Handoff

Before stopping, update `docs/ai/AI_HANDOFF.md` with:

- objective;
- work completed;
- files changed;
- commits or pull requests;
- tests executed and not executed;
- blockers and risks;
- exact next action;
- required human inputs.

A future contributor must be able to continue without chat history.
