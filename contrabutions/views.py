from django.shortcuts import render
from .models import Donation

def contrabution(request):
    donations = Donation.objects.all()
    return render(request, 'contrabution.html', {"donation": donations})
