from django.shortcuts import render

# This renders the contact us page.
def contact(request):
    return render(request, "contact.html")