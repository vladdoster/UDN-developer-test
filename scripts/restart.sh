#!/usr/bin/env bash

echo "Restarting local env"

docker-compose -f local.yml restart

echo "UDN collector is up at 0.0.0.0:8000"
