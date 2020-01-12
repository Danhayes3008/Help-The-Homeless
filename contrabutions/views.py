from django.shortcuts import render
from .models import Donations

def contrabution(request):
    donations = Donations.objects.all()
    return render(request, 'contrabution.html', {"donations": donations})
