from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth import views as auth_views

from core import views as core_views

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^', include('paytential.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^$', core_views.home, name='home'),
]
