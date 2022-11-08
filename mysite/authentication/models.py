from django.db import models
import uuid
from datetime import date

from django.conf import settings
# Create your models here.
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.db import IntegrityError, models
from django.urls import reverse
from django.utils.encoding import smart_bytes
from django.utils.http import urlsafe_base64_encode
from phonenumber_field.modelfields import PhoneNumberField

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.exceptions import ValidationError
class UserManager(BaseUserManager):
    def create_user(self, username, password=None,
                    **extra_fields):
        if username is None:
            raise TypeError('Users should have a username')
        user = self.model(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        try:
            user.save()
        except IntegrityError as e:
            if "authentication_user_username_key" in str(e):
                raise ValidationError({'username': 'username already exist'})
            if "authentication_user_email_polymorphic_ctype_id" in str(e):
                raise ValidationError({'email': 'email already exist'})

        return user

    def create(self, username, password,
               **extra_fields):
        return self.create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(
            username=username, password=password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
# Create your models here.
class User( AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=20, unique=True,
                                db_index=True)
  
    email = models.EmailField(
        max_length=255, db_index=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone_number = PhoneNumberField(db_index=True)
    birth_date = models.DateField(blank=False, null=False)
    full_name = models.CharField(max_length=150, blank=False, null=False)
   

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number', 'full_name', 'birth_date']

    objects = UserManager()
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    @property
    def age(self):
        today = date.today()
        one_or_zero = ((today.month, today.day) < (
            self.birth_date.month, self.birth_date.day))
        year_difference = today.year - self.birth_date.year
        age = year_difference - one_or_zero
        return age
