from django.shortcuts import render
from contrabutions.models import Donations

# Create your views here.
def index(request):
    donations = Donations.objects.all()
    return render(request, 'index.html', {"donations": donations})