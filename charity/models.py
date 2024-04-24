# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


# Create your models here.

class Owner(AbstractUser):
    gender_list = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other')
    )
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, )
    gender = models.CharField(max_length=1, choices=gender_list)
    avatar = models.ImageField(null=True)
    bio = models.TextField(null=True)
    bank_account = models.CharField(max_length=50, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='owner_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='owner_permissions')

    USERNAME_FIELD = "email"


class Charity(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='charity_logos', blank=True, null=True)
    total_donations = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    mission = models.CharField(max_length=500)
    creator = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
