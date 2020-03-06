from django.shortcuts import render, redirect, reverse
from contrabutions.models import Donation

# This view renders the cart page.
def view_donate(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")

# This view manages the part that adds the stuff to the cart
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

# This part allows the user to adjust the cart before going to the payment page
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