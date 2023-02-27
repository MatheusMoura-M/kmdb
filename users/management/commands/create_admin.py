from django.core.management.base import BaseCommand, CommandError
from users.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--username", type=str, help="Defina os campos")
        parser.add_argument("--email", type=str, help="Defina os campos")
        parser.add_argument("--password", type=str, help="Defina os campos")

    def handle(self, *args, **kwargs):
        username = kwargs.get("username")
        username = username if username else "admin"
        email = kwargs.get("email")
        email = email if email else f"{username}@example.com"
        password = kwargs.get("password")
        password = password if password else "admin1234"

        userFound = User.objects.filter(username=username).exists()
        emailFound = User.objects.filter(email=email).exists()

        if userFound:
            raise CommandError(f"Username `{username}` already taken.")

        if emailFound:
            raise CommandError(f"Email `{email}` already taken.")

        User.objects.create_superuser(username=username, email=email, password=password)

        self.stdout.write(
            self.style.SUCCESS(f"Admin `{username}` successfully created!")
        )
