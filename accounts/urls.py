from django.conf.urls import url, include
from accounts.views import login, logout, registration, profile, update_profile, delete_user
from accounts import url_reset

urlpatterns = [
    url(r'^login/', login, name="login"),
    url(r'^logout/', logout, name='logout'),
    url(r'^profile/', profile, name='profile'),
    url(r'^register/', registration, name='register'),
    url(r'^update/', update_profile, name='update_profile'),
    url(r'^password-reset/', include(url_reset)),
]