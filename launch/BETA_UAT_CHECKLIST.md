# Beta UAT Checklist

This checklist is the executable acceptance gate for the first limited beta release.

## 1. Environment readiness

- [ ] VPS is reachable through SSH using a non-root deploy user.
- [ ] Production environment variables exist only on the server or in GitHub Secrets.
- [ ] PostgreSQL and Redis containers are healthy.
- [ ] Backend health endpoint returns HTTP 200.
- [ ] Mini App and API are available over HTTPS.
- [ ] Database backup is created before deployment.

## 2. Telegram Mini App

- [ ] Bot opens the Mini App from Telegram.
- [ ] Telegram initData is validated by the backend.
- [ ] A new Telegram user is created once and reused on later sessions.
- [ ] Invalid or expired initData is rejected.
- [ ] Mini App works in Telegram mobile WebView.

## 3. Event and order flow

- [ ] Admin creates a draft event.
- [ ] Admin publishes the event.
- [ ] Published event is visible in the Mini App.
- [ ] User selects a ticket type and creates an order.
- [ ] Order starts in the pending state.
- [ ] Duplicate order attempts do not create duplicate billable orders.

## 4. Payment flow

- [ ] Payment session is created with the exact order amount and currency.
- [ ] Failed payment does not issue a ticket.
- [ ] Successful payment changes the order to paid.
- [ ] Repeated payment verification is idempotent.
- [ ] Unknown payment identifiers are rejected.

## 5. Ticket issuing and QR validation

- [ ] One paid order creates exactly one active ticket.
- [ ] Ticket can be retrieved using its order ID.
- [ ] Valid QR code is accepted before check-in.
- [ ] Unknown QR code is rejected.
- [ ] First check-in changes the ticket to checked_in.
- [ ] Second check-in is blocked with a conflict response.
- [ ] Cancelled or refunded tickets cannot enter.

## 6. Admin and operator acceptance

- [ ] Admin can view events, orders, payments, and issued tickets.
- [ ] Check-in operator can validate tickets without financial permissions.
- [ ] Sensitive admin actions are recorded in an audit log.
- [ ] Dashboard totals match database records.

## 7. Reliability and recovery

- [ ] Backend container restart does not lose persistent records.
- [ ] Database rollback occurs when ticket issuing fails inside a transaction.
- [ ] Database backup can be restored in a clean test environment.
- [ ] Health check detects database or Redis outages.
- [ ] Deployment rollback steps are documented and tested.

## 8. Beta release decision

The beta may launch only when:

- [ ] No open critical defects remain.
- [ ] No open high-severity payment or ticket defects remain.
- [ ] Full purchase-to-check-in flow passes on a real mobile device.
- [ ] Domain, SSL, backups, monitoring, and support contact are active.
- [ ] The release owner records a GO decision below.

## Sign-off

- Release version:
- Test date:
- VPS/environment:
- Tested by:
- Critical defects:
- High defects:
- Decision: GO / NO-GO
- Notes:
