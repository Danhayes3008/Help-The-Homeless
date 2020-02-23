from django.shortcuts import render
from contrabutions.models import Donation

# Create your views here.
def index(request):
    donations = Donation.objects.all()
    return render(request, 'index.html', {"donations": donations})