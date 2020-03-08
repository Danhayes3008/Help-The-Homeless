from django.shortcuts import render
from contrabutions.models import Donation

# This view renders the home page and witht the donations bit it allows us to donate to the charity.
def index(request):
    donations = Donation.objects.all()
    return render(request, 'index.html', {"donations": donations})