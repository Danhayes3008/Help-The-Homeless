from django.contrib import admin
from .models import total_homeless, yearly_homeless
# These lines of code allow us to use the models in the admin pannel
admin.site.register(total_homeless)
admin.site.register(yearly_homeless)
