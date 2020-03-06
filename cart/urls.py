from django.conf.urls import url
from .views import view_donate, amount_to_donate, adjust_donation
# These are the urls that help manage the donating and rendering of the cart page
urlpatterns = [
    url(r'^$', view_donate, name='view_donate'),
    url(r'^add/(?P<id>\d+)', amount_to_donate, name='amount_to_donate'),
    url(r'^adjust/(?P<id>\d+)', adjust_donation, name='adjust_donation'),
]
