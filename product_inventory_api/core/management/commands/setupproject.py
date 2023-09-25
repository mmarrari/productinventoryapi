import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Set up the project after initial clone'

import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Set up the project after initial clone'

    def handle(self, *args, **kwargs):

        self.stdout.write(self.style.SUCCESS('Running migrations...'))
        call_command("migrate")
        
        self.stdout.write(self.style.SUCCESS('Loading initial data...'))
        call_command("loaddata", "initial_products.json")
        
        self.stdout.write(self.style.SUCCESS('Creating superuser...'))

        username = os.environ.get('DJANGO_ADMIN_USER', 'admindj')
        email = 'admindj@exampledj.com'  
        password = os.environ.get('DJANGO_ADMIN_PASS', 'passdj')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully.'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser {username} already exists.'))

        self.stdout.write(self.style.SUCCESS('Starting the server...'))
        call_command("runserver", "0.0.0.0:8000")

