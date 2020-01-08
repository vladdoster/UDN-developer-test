#!/usr/bin/env bash

# Lets reduce input :)
#docker-compose -f local.yml run --rm django python manage.py createsuperuser

printf "Creating admin superuser"

docker-compose -f local.yml run --rm django python manage.py add_admin

printf "Superuser credentials are:\nusername: root\npassword: root"
