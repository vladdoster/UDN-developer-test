#!/usr/bin/env bash

echo "Tearing down local env"

docker-compose -f local.yml down

docker-compose -f local.yml build

echo "Applying migrations"

docker-compose -f local.yml run --rm django python manage.py makemigrations collector

echo "Starting stack"
docker-compose -f local.yml up

echo "UDN participant ingestion app is up at 0.0.0.0:8000"
