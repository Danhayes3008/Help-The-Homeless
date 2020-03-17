from django.conf.urls import url, include
from .views import contribution
# This is the url for the contribution page
urlpatterns = [
    url(r'^$', contribution, name="donation")]
