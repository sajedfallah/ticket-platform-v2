#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

if [[ ! -f .env.production ]]; then
  echo "Missing deployment/.env.production"
  exit 1
fi

set -a
# shellcheck disable=SC1091
source .env.production
set +a

: "${DOMAIN:?DOMAIN is required in .env.production}"
: "${SSL_EMAIL:?SSL_EMAIL is required in .env.production}"

if [[ "$DOMAIN" == "your-domain.com" ]] || [[ "$SSL_EMAIL" == "admin@your-domain.com" ]]; then
  echo "Replace placeholder DOMAIN and SSL_EMAIL values before enabling SSL."
  exit 1
fi

if ! [[ "$DOMAIN" =~ ^([A-Za-z0-9-]+\.)+[A-Za-z]{2,}$ ]]; then
  echo "Invalid DOMAIN: $DOMAIN"
  exit 1
fi

COMPOSE=(docker compose -f docker-compose.prod.yml)

echo "Starting HTTP stack for ACME validation..."
"${COMPOSE[@]}" up -d --build nginx backend mini-app admin-panel

echo "Requesting Let's Encrypt certificate for $DOMAIN..."
"${COMPOSE[@]}" --profile tools run --rm certbot certonly \
  --webroot \
  --webroot-path /var/www/certbot \
  --domain "$DOMAIN" \
  --email "$SSL_EMAIL" \
  --agree-tos \
  --no-eff-email \
  --non-interactive

cp nginx/nginx.conf "nginx/nginx.http.conf.backup"
sed "s/__DOMAIN__/${DOMAIN//\//\\/}/g" \
  nginx/nginx.ssl.conf.template > nginx/nginx.conf

echo "Validating and rebuilding Nginx with TLS configuration..."
"${COMPOSE[@]}" build nginx
"${COMPOSE[@]}" up -d nginx
"${COMPOSE[@]}" exec -T nginx nginx -t

 echo "Starting automatic certificate renewal service..."
"${COMPOSE[@]}" --profile ssl up -d certbot-renew

STATUS_URL="https://${DOMAIN}/nginx-health"
echo "SSL enabled. Verify: $STATUS_URL"
echo "Note: nginx/nginx.conf is rendered locally. Re-run this script after a clean checkout or if the HTTP template replaces it."
