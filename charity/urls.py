"""charity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from homepage.views import index
from accounts import urls as urls_accounts
from contact import urls as urls_contact
from about import urls as urls_about
from contrabutions import urls as urls_donation
from cart import urls as urls_cart
from payment import urls as urls_payment
from django.views import static
from .settings import MEDIA_ROOT
# These are all the imported urls and one that deal with the media root
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^contact/', include(urls_contact)),
    url(r'^about_us/', include(urls_about)),
    url(r'^contribution/', include(urls_donation)),
    url(r'^cart/', include(urls_cart)),
    url(r'^payment/', include(urls_payment)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
