"""
Database models.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

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
    is_staff = models.BigAutoField(default=False)

    # username defines the field that we want to use for authentication,
    # and this how we replace the username that comes with default user model
    USERNAME_FILED = 'email'

