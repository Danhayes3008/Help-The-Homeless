from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from accounts.views import change_password, login, logout, profile, registration, update_profile
from accounts import url_reset
# This is a list of the urls for the accounts app
urlpatterns = [
    url(r'^login/', login, name="login"),
    url(r'^logout/', logout, name='logout'),
    url(r'^profile/', profile, name='profile'),
    url(r'^register/', registration, name='register'),
    url(r'^update/', update_profile, name='update_profile'),
    url(r'^change_password/', views.change_password, name='change_password'),
    url(r'^password_reset/', include(url_reset)),
]