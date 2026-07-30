# Ticket Platform v2 - End To End Test Plan

## Services

- PostgreSQL
- Redis
- Backend API
- Telegram Bot
- Mini App
- Admin Panel
- Nginx Gateway

## User Flow

1. Open Telegram Bot
2. Launch Mini App
3. Browse Events
4. Select Ticket Type
5. Create Order
6. Complete Payment
7. Issue Ticket
8. Display QR Code
9. Validate QR at Check-in

## Admin Flow

1. Login
2. View Dashboard
3. Check Orders
4. Review Payments
5. Validate Entry
6. Export Reports

## API Checks

- GET /health
- Events endpoints
- Order creation
- Ticket issuance
- Ticket validation
