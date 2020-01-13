from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import IntegrityError


class Command(BaseCommand):
    def handle(self, **options):
        try:
            User.objects.create_superuser('root', 'admin@example.com', 'root')
            print('\n')
        except IntegrityError as e:
            print("\nAdmin already exists!")
