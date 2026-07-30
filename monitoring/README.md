# Production Monitoring Foundation

## Health Checks

Services should expose health endpoints for:

- Backend API
- Database connection
- Redis connection
- Telegram bot worker

## Logging

Production logs should include:

- Request ID
- User ID when available
- Order ID
- Payment ID
- Ticket ID
- Error context

## Metrics

Recommended metrics:

- API response time
- Payment success rate
- Ticket issuance count
- QR validation count
- Check-in failures

## Alerts

Critical alerts:

- Backend unavailable
- Database connection failure
- Payment callback errors
- High check-in rejection rate
