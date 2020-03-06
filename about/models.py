# These models are not needed at all but i have left them in so that the admin could record the information that would be needed for the charts 
from django.db import models
# This model is used to store what the total homeless is
class total_homeless(models.Model):
    name = models.CharField(max_length=250, default="")
    totalHomeless = models.DecimalField(max_digits=9, decimal_places=0)
    totalPopulation = models.DecimalField(max_digits=9, decimal_places=0)
    
    class Meta:
        verbose_name_plural = "Total_Homeless"
    
    def __str__(self):
        return self.name
# This model is used to show the yearly homeless totals
class yearly_homeless(models.Model):
    name = models.CharField(max_length=250, default="")
    year = models.DecimalField(max_digits=4, decimal_places=0)
    total = models.DecimalField(max_digits=9, decimal_places=0)
    
    class Meta:
        verbose_name_plural = "Yearly_Homeless"
    
    def __str__(self):
        return self.name