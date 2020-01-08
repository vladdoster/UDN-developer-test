#!/usr/bin/env bash

echo "Restarting local env"

docker-compose -f local.yml restart

echo "Assay viz is up at 0.0.0.0:8000"
