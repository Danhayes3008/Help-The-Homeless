from django.db import models
from contrabutions.models import Donation
from accounts.models import Profile
from django.contrib.auth.models import User

# Create your models here.

#This model will be used to hold all the information needed to submit donations, it will also be used to help display the users donation history
class Details(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="donation_details", null=True, blank=True)
    street_address_1 = models.CharField(max_length=40, blank=False)
    street_address_2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.profile)

# This model holds the list of what was paid for and the amounts 
class DonateLineItem(models.Model):
    details = models.ForeignKey(Details, related_name="lineitems")
    donation = models.ForeignKey(Donation, null=False)
    quantity = models.IntegerField(blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.id, self.quantity, self.details.profile, self.donation.name, self.donation.donation_amount)
