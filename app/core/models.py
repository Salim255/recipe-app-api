"""
Database models.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# We define the user manager baser on the base user manger class provided by Django
class UserManager(BaseUserManager):
    """Manager for users."""

    # password=None, so we can provided optionally the password or not
    # in case we create use that doesn't have a password
    # extra_field and it's means that we can provide keyword arguments ,
    # any number of keyword arguments that will be passed into our model.
    # this useful when we define additional fields, for example, a name,
    # you can pass it as an extra field and that will be automatically
    # created when the user model is created
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""

        # self.model because our manager is associated to a model,
        # we need a way of being able to access the model that we're associated with
        user = self.model(email=email, **extra_fields)

        # set.password method on our object, and this will set the encrypted password
        # so it will take the password that's provided in the create user method
        user.set_password(password)

        # Then we call user safe and this saves the user model and we're passing in self._db,
        # This just to support adding multiple database if
        # you choose to add multiple database to your project.
        # It's best practice to pass in self._db, whenever you are creating
        # or saving a new object using a user manager
        user.save(using=self._db)

        return user

# AbstractBaseUser contains the functionality for the
# authentication system but not any field

# PermissionsMixin contains the functionality for
# permissions feature of Django and also contains
# any fields that are needed for the permissions feature
class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""

    email = models.EmailField(max_length=255 , unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # This just to assign this user manager to our custom user class
    # And we do that by typing objects=UserManager()
    # And this is how to assign a user manger inDjango
    objects = UserManager()

    # username defines the field that we want to use for authentication,
    # and this how we replace the username that comes with default user model
    USERNAME_FIELD = 'email'


