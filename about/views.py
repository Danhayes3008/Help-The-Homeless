from django.shortcuts import render
from .models import total_homeless, yearly_homeless

# This renders the about page
def about(request):
    return render(request, "about.html")