from django.contrib import admin
from .models import Donation
# This line of code registers the donation model so we can access it in the admin pannel
admin.site.register(Donation)
