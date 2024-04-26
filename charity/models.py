# Create your models here.
import os

from django.contrib.auth.models import AbstractBaseUser, Group, Permission
from django.db import models

def upload_path(instance, filename):
    # Generate a unique filename based on the model instance and filename
    base_filename, file_extension = os.path.splitext(filename)
    model_name = instance.__class__.__name__.lower()
    return f'{model_name}s/{instance.email}/{base_filename}{file_extension}'
# Create your models here.

class Owner(AbstractBaseUser):
    gender_list = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other')
    )
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, )
    gender = models.CharField(max_length=1, choices=gender_list)
    avatar = models.ImageField(null=True,blank = True, upload_to=upload_path)
    bio = models.TextField(null=True)
    bank_account = models.CharField(max_length=50, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='owner_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='owner_permissions')
    role = models.CharField(max_length=10,  default='owner', editable=False)

    USERNAME_FIELD = "email"


class Charity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to=upload_path, blank=True, null=True)
    total_donations = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    mission = models.CharField(max_length=500)
    creator = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
