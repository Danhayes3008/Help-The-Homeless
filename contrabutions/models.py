from django.db import models

# This is the model that allows us to create an item for managing the donations with.
class Donation(models.Model):
    name = models.CharField(max_length=254, default='')
    donation_amount = models.DecimalField(max_digits=9, decimal_places=2, default='1.00')
    # This class sets the name of the table in the admin pannel 
    class Meta:
        verbose_name_plural = "Donation"
        
    def __str__(self):
        return self.name