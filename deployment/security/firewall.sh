#!/bin/bash
set -e

# Basic production firewall setup
ufw default deny incoming
ufw default allow outgoing
ufw allow ssh
ufw allow http
ufw allow https
ufw --force enable

echo "Firewall configured"
