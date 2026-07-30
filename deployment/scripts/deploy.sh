#!/bin/bash
set -e

echo "Starting Ticket Platform v2 deployment"

cd "$(dirname "$0")/.."

if [ ! -f .env.production ]; then
  echo "Missing .env.production"
  exit 1
fi

docker compose -f docker-compose.prod.yml pull

docker compose -f docker-compose.prod.yml up -d --build

docker compose -f docker-compose.prod.yml ps

echo "Deployment completed"
