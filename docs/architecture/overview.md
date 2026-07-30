# Architecture Overview

## Purpose

Ticket Platform v2 provides an event-ticketing workflow centered on Telegram access, event discovery, orders, payments, ticket issuance, QR validation, check-in, administration, and deployment.

## System Context

```text
Telegram User
  -> Telegram Bot
  -> Telegram Mini App
  -> Nginx
  -> FastAPI Backend
  -> PostgreSQL / Redis

Administrator
  -> Admin Panel
  -> Nginx
  -> FastAPI Backend

Check-in Operator
  -> QR validation endpoint
  -> Ticket persistence
```

## Runtime Components

### Backend

- FastAPI application
- API routers for health, events, orders, tickets, and payments
- SQLAlchemy models and services
- Alembic migration tooling
- Provider abstraction for payment integration

### Data Layer

- PostgreSQL is the intended system of record.
- Redis is available for caching or transient runtime concerns.
- Database-backed behavior must take precedence over in-memory placeholders in production paths.

### Client Surfaces

- Telegram Bot
- Telegram Mini App
- Admin Panel

### Edge and Deployment

- Nginx routes `/api/`, `/app/`, and `/admin/`.
- Docker Compose defines application services and infrastructure dependencies.
- Certbot and Let's Encrypt provide the intended TLS bootstrap.

## Core Domain Areas

- Users
- Organizers
- Events
- Ticket types
- Orders
- Payments
- Tickets
- Check-ins
- Refunds and settlements (planned or partially designed)

## Architectural Boundaries

1. Payment providers must be accessed through an adapter/provider abstraction.
2. Ticket issuance must follow successful, verified, and idempotent payment completion.
3. Check-in must reject invalid, inactive, or already-used tickets.
4. Production state must be persisted in PostgreSQL.
5. Secrets must never be committed to Git.
6. Deployment status must never be inferred from configuration files alone.
7. Architecture changes require an ADR.

## Current Limitations

- Authentication and authorization architecture is not yet canonically documented or fully verified.
- API contracts are not fully documented.
- A complete executable migration chain is not yet verified.
- Frontend and Telegram runtime behavior are not yet verified in a deployed environment.
- Real payment, refund, settlement, and organizer workflows are incomplete or unverified.

## Verification Rule

A component is `IMPLEMENTED` when code exists. It is `TESTED` only when tests have passed, `DEPLOYED` only when released to an environment, and `VERIFIED` only after behavior is validated in that environment.
