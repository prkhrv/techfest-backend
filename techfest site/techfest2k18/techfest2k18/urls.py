"""techfest2k18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from fest_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',views.index,name='home'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('me01/',views.me01,name='me01'),
    path('me02/',views.me02,name='me02'),
    path('mba01/',views.mba01,name='mba01'),
    path('ece01/',views.ece01,name='ece01'),
    path('cse01/',views.cse01,name='cse01'),
    path('it01/',views.it01,name='it01'),
    path('mca01/',views.mca01,name='mca01'),
    path('mca02/',views.mca02,name='mca02'),
    path('ch01/',views.ch01,name='ch01'),
    path('en01/',views.en01,name='en01'),
    path('en02/',views.en02,name='en02'),
    path('civ01/',views.civ01,name='civ01'),
    path('bt01/',views.bt01,name='bt01'),
    path('bph01/',views.bph01,name='bph01'),
    path('bph02/',views.bph02,name='bph02'),
    path('success/',views.success,name='success'),
]
