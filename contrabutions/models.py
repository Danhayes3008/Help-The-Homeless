from django.db import models

# Create your models here.
class Donations(models.Model):
    name = models.CharField(max_length=254, default='')
    donation = models.DecimalField(max_digits=9, decimal_places=2, default='1.00')
    minDonation = models.DecimalField(max_digits=9, decimal_places=2, default='1.00')
    
    class Meta:
        verbose_name_plural = "Donations"
        
    def __str__(self):
        return self.name