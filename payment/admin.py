from django.contrib import admin
from .models import donate, DonateLineItem
# Register your models here.

class DonateLineAdminInline(admin.TabularInline):
    model = DonateLineItem
    
class DonateAdmin(admin.ModelAdmin):
    inlines = (DonateLineAdminInline, )
    
admin.site.register(donate, DonateAdmin)