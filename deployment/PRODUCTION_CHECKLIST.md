# Production Deployment Checklist

## Services

- [ ] PostgreSQL container running
- [ ] Redis container running
- [ ] Backend health endpoint responding
- [ ] Telegram bot service connected
- [ ] Mini App build completed
- [ ] Admin Panel build completed
- [ ] Nginx routing verified

## Verification

```bash
docker compose up --build
```

Health checks:

- `/health`
- `/api/events`
- `/api/tickets/validate`
