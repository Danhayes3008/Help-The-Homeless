from django.shortcuts import render
from .models import Donation
# This view renders the page and searches for all items in the Donation table
def contribution(request):
    donations = Donation.objects.all()
    print(donations)
    return render(request, 'contribution.html', {"donations": donations})
