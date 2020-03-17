# This file contains the view that allows payments to be made
from django.shortcuts import render, get_object_or_404,     reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms  import MakePaymentForm, DetailsForm
from .models import DonateLineItem
from django.conf import settings 
from django.utils import timezone
from contrabutions.models import Donation
import stripe
# This is the stripe api key that connects the site to stripe
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def payment (request):
    if request.method=="POST":
        details_form = DetailsForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        # This part checks to see if the forms were filled out correctly
        if details_form.is_valid() and payment_form.is_valid():
            donate = details_form.save(commit=False)
            donate.profile = request.user.profile
            donate.date = timezone.now()
            donate.save()
            
            cart = request.session.get('cart', {})
            total = 0
            # This part creates the receipt of the sale
            for donation_id, quantity in cart.items():
                donation = get_object_or_404(Donation, pk=donation_id)
                total += quantity * donation.donation_amount
                donate_line_item = request.user
                donate_line_item = DonateLineItem(
                    details = donate,
                    donation = donation,
                    quantity = quantity
                )
                donate_line_item.save()
            # This part tries to charge the card used by the user
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Sorry, your card was Declined!")
                
            if customer.paid:
                messages.error(request, "You have successfully Paid!")
                request.session['cart'] = {}
                return redirect(reverse('donation'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(request, "We were unable to take payment with that card!")
    else:
        payment_form = MakePaymentForm()
        donate_form = DetailsForm()
        
    return render(request, "payment.html", {
        'donate_form': donate_form,
         'payment_form': payment_form,
          'publishable': settings.STRIPE_PUBLISHABLE})