import secrets
import string

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import call_command


def generate_password(length: int = 10) -> str:
    characters = string.digits + string.punctuation + string.ascii_letters
    return "".join(secrets.choice(characters) for _ in range(length))

def database_setup():
    """
    A series of database preparations, depending on settings.DEBUG variable,
    mainly designed for server startup stage.
    """
    print(">>> Debug Activated: ", settings.DEBUG)
    print(">>> Database:        ", settings.DATABASES["default"]["NAME"])

    print(">>> Running migrations...")
    call_command(command_name="migrate")

    print(f">>> Creating superuser...")
    superuser_created = False  # controls message about Django Admin credentials
    username = "grp-admin"
    password = generate_password()
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, password=password, email=username + '@example.com')
        superuser_created = True

    print(">>> Importing movies...")
    call_command(command_name="import_worst_movies_dataset")
    if superuser_created:
        print(f">>> Access Django Admin with the following credentials: '{username}' / '{password}'")
    else:
        print(">>> Refer to project documentation for Django Admin credentials.")

    if not settings.DEBUG:
        print(">>> Django Shell does not have access to in-memory database of another process.")

    print(">>> Done!")

