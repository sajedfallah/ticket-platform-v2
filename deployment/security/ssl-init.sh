#!/bin/bash
set -e

# SSL setup placeholder for Let's Encrypt deployment
# Requires certbot installation on VPS

DOMAIN=${1}
EMAIL=${2}

if [ -z "$DOMAIN" ] || [ -z "$EMAIL" ]; then
  echo "Usage: ./ssl-init.sh domain email"
  exit 1
fi

certbot --nginx -d "$DOMAIN" --email "$EMAIL" --agree-tos --non-interactive

echo "SSL configured"
