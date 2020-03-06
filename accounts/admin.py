from django.contrib import admin
from .models import Profile

# This registers the profile model.
admin.site.register(Profile)
# This line of code renames the admin panels site header
admin.site.site_header = 'Help The Homeless Administration'