#!/bin/bash
set -e

BACKUP_DIR="./backups"
mkdir -p "$BACKUP_DIR"

DATE=$(date +%Y-%m-%d_%H-%M-%S)

DB_CONTAINER=$(docker ps --filter name=postgres -q | head -1)

if [ -z "$DB_CONTAINER" ]; then
  echo "PostgreSQL container not found"
  exit 1
fi

docker exec "$DB_CONTAINER" pg_dump -U $POSTGRES_USER $POSTGRES_DB > "$BACKUP_DIR/db_$DATE.sql"

echo "Backup created: db_$DATE.sql"
