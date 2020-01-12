from django.conf.urls import url, include
from accounts.views import login, logout, registration, profile, update
from accounts import url_reset

urlpatterns = [
    url(r'^login/', login, name="login"),
    url(r'^logout/', logout, name='logout'),
    url(r'^profile/', profile, name='profile'),
    url(r'^register/', registration, name='register'),
    url(r'^update/', update, name='update'),
    url(r'^password-reset/', include(url_reset)),
]