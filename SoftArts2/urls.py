"""SoftArts2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from SoftArts2 import settings
from general.views import index as main_page

urlpatterns = [
    url(r'^$', main_page, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', 'general.views.login', name='login'),
    url(r'^logout/', 'general.views.logout', name='logout'),
    url(r'^register/', 'general.views.register', name='register'),
    url(r'^music/', include('music.urls', namespace='music')),
    url(r'^pictures/', include('pictures.urls', namespace='pictures')),
    url(r'^literature/', include('literature.urls', namespace='literature')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
