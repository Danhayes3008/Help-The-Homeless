from django.conf.urls import url, include
from .views import contribution

urlpatterns = [
    url(r'^$', contribution, name="donation"),
]
