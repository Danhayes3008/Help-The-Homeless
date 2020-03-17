from django.conf.urls import url
from .views import payment
# This url pattern holds the url for the payment page
urlpatterns = [
    url(r'^$', payment, name='payment'),]