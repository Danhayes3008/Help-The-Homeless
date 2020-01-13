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