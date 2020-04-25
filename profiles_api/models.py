from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.
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
    



