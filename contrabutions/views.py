from django.shortcuts import render

def contrabution(request):
    donations = Donations.objects.all()
    return render(request, 'contrabution.html', {"donations": donations})
