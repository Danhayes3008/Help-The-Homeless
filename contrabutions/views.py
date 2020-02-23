from django.shortcuts import render
from .models import Donation

def contrabution(request):
    donations = Donation.objects.all()
    print(donations)
    return render(request, 'contrabution.html', {"donations": donations})
