from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.models import BaseUserManager


# Create your models here which create DB in e.g. Postgres.
class UserProfileManager(BaseUserManager):
    """ Manager for user profiles """

    def create_user(self, email, name, password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError('User must have an email address')

        # standardize 2nd part of email address, as it
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)  # encrypt password, convert to harsh
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """ Create and save a new superuser with given details """
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # is_active -> a field for a permission system; determine is a user active or not
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # to work with Django admin and Django authentication system
    # instead of providing user name and password, a user provide email and password
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # functions to interact with our custom user model
    def get_full_name(self):
        """ Retrieve a full name of user """
        return self.name

    def get_short_name(self):
        """ Retrieve a short name of user """
        return self.name

    def __str__(self):
        """ Return string representation of our user """
        return self.email
