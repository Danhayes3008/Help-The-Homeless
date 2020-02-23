from django.shortcuts import render, redirect, reverse
from contrabutions.models import Donation

# Create your views here.
def view_donate(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def amount_to_donate(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('donation'))


def adjust_donation(request, id):
    """
    Adjust the quantity of the specified donation to the specified
    amount
    """
    print(request.POST)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_donate'))