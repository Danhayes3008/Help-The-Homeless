from django.conf.urls import url, include
from .views import contrabution

urlpatterns = [
    url(r'^$', contrabution, name="donation"),
]
