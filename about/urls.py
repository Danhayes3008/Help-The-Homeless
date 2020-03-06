from django.conf.urls import url, include
from .views import about
# The url for the about page
urlpatterns = [
    url(r'^about/', about, name="about")
]
