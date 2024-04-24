from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


# Create your models here.

class Donor(AbstractUser):
    gender_list = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other')
    )
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=1, choices=gender_list, null=True)
    total_donated = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    groups = models.ManyToManyField(Group, related_name='donor_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='donor_permissions')

    USERNAME_FIELD = "email"
