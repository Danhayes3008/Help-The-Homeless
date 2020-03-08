from django.contrib import admin
from .models import Details, DonateLineItem
# These classes deal with linking the two models together and displaying them in the admin pannel.

class DonateLineAdminInline(admin.TabularInline):
    model = DonateLineItem
    
class DonateAdmin(admin.ModelAdmin):
    inlines = (DonateLineAdminInline, )
    
admin.site.register(Details, DonateAdmin)