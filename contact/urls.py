from django.conf.urls import url
from .views import contact
# This is the url for the contact us page
urlpatterns = [
    url(r'^$', contact, name='contact')]
