"""cookbook URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('Falcon.urls',namespace='Falcon')),
    url(r'^',include('Beginner.urls',namespace='Beginner')),
    url(r'^',include('Moderate.urls',namespace='Moderate')),
    url(r'^',include('Advanced.urls',namespace='Advanced')),
    url(r'^',include('django.contrib.auth.urls')),
    url(r'^',views.Test.as_view(),name='test'),
    url(r'^',views.Thanks.as_view(),name='thank'),
    url(r'',include('Falcon.urls')),


]
