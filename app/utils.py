import logging
import secrets
import string

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import call_command

log = logging.getLogger()

def generate_password(length: int = 10) -> str:
    characters = string.digits + string.punctuation + string.ascii_letters
    return "".join(secrets.choice(characters) for _ in range(length))

def database_setup():
    """
    A series of database preparations, depending on settings.DEBUG variable,
    mainly designed for server startup stage.
    """
    log.info("running migrations")
    call_command(command_name="migrate")

    log.info("creating superuser")
    superuser_created = False  # controls message about Django Admin credentials
    username = "grp-admin"
    password = generate_password()
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, password=password, email=username + '@example.com')
        superuser_created = True

    log.info("importing movies dataset")
    call_command(command_name="import_worst_movies_dataset")
    if superuser_created:
        print(f"\n>>> Access Django Admin with the following credentials: '{username}' / '{password}'\n")
    else:
        log.info(f"refer to project documentation (README) for Django Admin credentials")

    if not settings.DEBUG:
        log.warning(f"in-memory database belongs to server process - Django Shell will not be able to access it")

    log.info("database setup finished!")

