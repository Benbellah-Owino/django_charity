from django.db import models

from donor.models import Donor
from charity.models import Charity

# from DonationSystem.charity.models import Charity
# Create your models here.

class Donation(models.Model):
    reference_msg = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    donor = models.ForeignKey(Donor, on_delete=models.SET_NULL, null = True, related_name='donations')
    charity = models.ForeignKey(Charity, on_delete=models.DO_NOTHING, related_name='donations')
    date = models.DateTimeField(auto_now_add=True)
