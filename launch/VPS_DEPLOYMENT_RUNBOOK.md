# VPS Deployment Runbook

This runbook deploys Ticket Platform v2 on a fresh Ubuntu VPS using the existing production Docker Compose stack.

## 1. Required information

Prepare these non-secret values:

- VPS public IP
- SSH username
- Primary domain
- API subdomain
- Mini App subdomain
- Admin subdomain

Keep passwords, bot tokens, JWT secrets, and payment keys outside Git.

## 2. DNS records

Create A records pointing to the VPS IP:

- `api.example.com`
- `app.example.com`
- `admin.example.com`

Wait until all three names resolve to the VPS before requesting SSL certificates.

## 3. Initial VPS setup

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git curl ca-certificates ufw
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker "$USER"
newgrp docker
sudo systemctl enable --now docker
```

Open only required ports:

```bash
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
sudo ufw status
```

## 4. Clone the repository

```bash
sudo mkdir -p /opt/ticket-platform
sudo chown "$USER":"$USER" /opt/ticket-platform
git clone https://github.com/sajedfallah/ticket-platform-v2.git /opt/ticket-platform
cd /opt/ticket-platform
```

## 5. Create production environment

```bash
cd /opt/ticket-platform/deployment
cp .env.production.example .env.production
nano .env.production
```

Replace every placeholder. At minimum configure:

```env
APP_ENV=production
BACKEND_PORT=8000
JWT_SECRET=<strong-random-secret>
CORS_ORIGINS=https://app.example.com,https://admin.example.com

POSTGRES_DB=ticket_platform
POSTGRES_USER=ticket_platform
POSTGRES_PASSWORD=<strong-database-password>
DATABASE_URL=postgresql://ticket_platform:<password>@postgres:5432/ticket_platform

REDIS_URL=redis://redis:6379/0

TELEGRAM_BOT_TOKEN=<bot-token>
TELEGRAM_WEBAPP_URL=https://app.example.com

PAYMENT_PROVIDER_KEY=<provider-key-or-test-key>

DOMAIN=example.com
SSL_EMAIL=admin@example.com
```

Protect the file:

```bash
chmod 600 .env.production
```

## 6. Validate the compose configuration

```bash
cd /opt/ticket-platform/deployment
docker compose --env-file .env.production -f docker-compose.prod.yml config
```

Do not continue if this command reports missing variables or invalid paths.

## 7. First deployment

```bash
chmod +x scripts/deploy.sh
./scripts/deploy.sh
```

The current stack builds and starts PostgreSQL, Redis, Backend, Telegram Bot, Mini App, Admin Panel, and Nginx.

Verify containers:

```bash
docker compose -f docker-compose.prod.yml ps
docker compose -f docker-compose.prod.yml logs --tail=100 backend
docker compose -f docker-compose.prod.yml logs --tail=100 nginx
```

## 8. Health checks

Test locally on the VPS first:

```bash
curl -i http://127.0.0.1/
curl -i http://127.0.0.1/health
```

Then test public routes after DNS and Nginx are configured:

```bash
curl -i https://api.example.com/health
curl -I https://app.example.com
curl -I https://admin.example.com
```

## 9. SSL prerequisites

Before SSL issuance confirm:

```bash
getent hosts api.example.com
getent hosts app.example.com
getent hosts admin.example.com
```

Each result must show the VPS public IP. Then run the repository SSL initialization script according to its documented arguments.

## 10. Telegram setup

In BotFather set the Mini App/Web App URL to:

```text
https://app.example.com
```

Do not place the bot token in source code. Store it only in `.env.production` on the VPS or in a protected deployment secret.

## 11. Deployment update procedure

```bash
cd /opt/ticket-platform
git pull --ff-only origin main
cd deployment
./scripts/backup.sh
./scripts/deploy.sh
```

After every update verify health, payment creation, ticket issuance, and QR check-in before inviting users.

## 12. Rollback procedure

If a release fails:

```bash
cd /opt/ticket-platform
git log --oneline -10
git checkout <previous-good-commit>
cd deployment
./scripts/deploy.sh
```

Restore the latest verified database backup only when the database schema or data was damaged. Never overwrite a healthy database without first creating another backup.

## 13. Beta launch gate

Do not open the Beta until all items in `launch/BETA_UAT_CHECKLIST.md` are approved, including:

- HTTPS active
- database backup verified
- Telegram authentication verified
- successful and failed payment paths tested
- one ticket per paid order confirmed
- duplicate QR check-in blocked
- admin and operator permissions verified

## Operator inputs still required

The repository can prepare deployment files, but the server owner must provide or configure:

- VPS access
- DNS records
- production environment secrets
- BotFather Web App URL
- payment provider credentials
