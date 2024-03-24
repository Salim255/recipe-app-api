"""
Django command to wait for the database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2Error
# Error when database isn't ready

from django.db.utils import OperationalError
# Error that Django throws when database isn't ready

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """"Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        # To logout in the screen the message waiting for ...

        # Here we assume that database is not up, until we know that it's
        db_up = False

        while db_up is False:
            try:

                # We call this check and if database is isn't ready this will
                # throw an exception else we set db_up to true
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                # If we get here with Psycopg2Error or OperationalError,
                # then we're going to print to the screen database unavailable,
                # and wait for one second and then to call time to sleep and
                # then with the value one which says sleep for one second

                # So Python is going to stop here for one second and then it's
                # going to continue with the loop and try again.
                # This way we keep trying the database.
                # It's keep logging to the screen so we know
                # when the database is available and
                # then we can reliably start our application.

                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        # To have nice green success message
        self.stdout.write(self.style.SUCCESS('Database available!'))
