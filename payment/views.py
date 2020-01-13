from django.shortcuts import render, get_object_or_404,     reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms  import MakePaymentForm, DonateForm
from .models import OrderLineItem
from django.conf import settings 
from django.utils import timezone
from contrabutions.models import Donations
import stripe

stripe.api_key = settings.STRIPE_KEY

@login_required()
def payment (request):
    if request.method=="POST":
        donate_form = DonateForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if donate_form.is_valid() and payment_form.is_valid():
            donate = donate_form.save(commit=False)
            donate.date = timezone.now()
            donate.save()
            
            cart = request.session.get('cart', {})
            total = 0
            for id, amount in cart.items():
                total += amount * donations.price
                donate_line_item = DonateLineItem(
                    donate = donate,
                    donations = donations,
                    amount = amount,
                )
            donate_line_item.save()