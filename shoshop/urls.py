"""shoshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

import mainapp.views as mainapp
import comapp.views as comapp

urlpatterns = [

    path('', mainapp.main, name='main'),
    path('list_of_deals/', include('mainapp.urls',
                                   namespace='dl')),
    path('list_of_companies/', include('comapp.urls',
                                       namespace='com')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('', include('social_django.urls', namespace='social')),
    path('admin/', include('adminapp.urls', namespace='admin')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('order/', include('ordersapp.urls', namespace='order')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
