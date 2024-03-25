"""
Test for models.
"""

from django.test import TestCase # Base class for our

# get_user_model it's a function provided by django in order to
# the default user model for the project
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""

        email = 'test@example.com'
        password = 'testpass123'

        # We get the user model by calling get user model
        # Then we call objects, which is a reference to the manager that we are going to create
        # Then we call the create user method by email & password
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)

        # Check password method is provided by the default model manager that we added to our project
        self.assertTrue(user.check_password(password))