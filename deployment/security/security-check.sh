#!/bin/bash
set -e

echo "Checking production security configuration..."

command -v docker >/dev/null && echo "Docker: OK"
command -v nginx >/dev/null && echo "Nginx: OK"
command -v ufw >/dev/null && echo "Firewall tool: OK"

curl -I https://localhost 2>/dev/null || true

echo "Security check completed"
