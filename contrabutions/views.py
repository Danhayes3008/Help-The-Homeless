from django.shortcuts import render
from .models import Donation

def contribution(request):
    donations = Donation.objects.all()
    print(donations)
    return render(request, 'contribution.html', {"donations": donations})
