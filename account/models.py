from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, username, firstname, lastname, password=None, **extra_fields):
        if not username:
            raise ValueError("Must input a Username")
        if not email:
            raise ValueError( "Must have a valid email address")
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username, 
            firstname=firstname,
            lastname=lastname,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, firstname, lastname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, firstname, lastname, password=password, **extra_fields)
    

class USERS(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=30, unique=True)
    username = models.CharField(max_length=30, unique=True, null=True, blank=True)
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/user-default.png', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    wallet = models.IntegerField(default=0)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', "firstname", "lastname"]

    def __str__(self):
        return self.email
