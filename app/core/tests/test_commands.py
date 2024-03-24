"""
Test custom Django management commands
"""

from unittest.mock import patch  # In order to mock behavior of the database

from psycopg2 import OperationalError as Psycopg2Error
# ts one of the possibility of error that we might get when we
# try to connect to database before database is ready

from django.core.management import call_command
# It's a helper function provided by Django
# allows us to call a command that we testing

from django.db.utils import OperationalError
# Another exceptional error we might get through by the database
# depending on what stage of the start up process it is.

from django.test import SimpleTestCase
# The simple test case, which is the base test class that we're
# going to use for testing our unit test or creating our unit test
# Its import that we use a simple test case because we e testing
# behavior that the database is not available and therefore we do need
# migrations and things like that to applied to the test"""


@patch("core.management.commands.wait_for_db.Command.check")
class CommandTests(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database ready."""

        """ Here we tell when we call check or
        when check is called inside our
        command, inside our test case, we jest
        want it to return the true value"""
        patched_check.return_value = True

        call_command('wait_for_db')
        """This will execute the code inside wait for db and also check where
        the database is ready and also checks that the command is
        set up correctly and can be called inside our Django project"""

        # Check if that check method has been called
        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting OperationalError."""

        """ Side effect allows you to pass in various different items that
        get handled differently depending on that type.
        So if we pass in an exception,
        then the mocking library knows that it should raise that exception.
        If we pass in a boolean, then it will return the boolean value.
        So what this allows us to do is to define various different values
        that happen each time we call it in the order that we call it. """

        """So Basically what we are doing here is we're saying the
        first two times we call the mocked method,
        we want it to raise the Psycopg2Error, so it raises the error,
        and the next three times we raise OperationalError"""

        """There are different stages of Postgres starting,
         the first stages is the application itself hasn't even started yet,
         so it's not ready to accept any connections.
         In that case, you get the Psycopg2Error which
         is raised from the psycopg2 package.
         The second stage when the database is ready to accept connections,
         but it hasn't set up the testing database that we want to use,
        so it hasn't created the dev database that we want to use,
        in that case, Django raise the OperationalError
        from from Django exceptions.
        so it's two different exceptions. Finally  we have true,
        which means the sixth time we call it, we're going to get true back,
        so it's jus going to return true"""

        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)

        """Make sure that patched_check being
        called with database equals default, """
        patched_check.assert_called_with(databases=['default'])
