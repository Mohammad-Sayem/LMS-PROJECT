"""LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from polls import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path("", views.index, name="index"),
   path("admin1", views.admin1, name="admin1"),
   path("messages", views.messages, name="messages"),
   path("courses", views.courses, name="courses"),
   path("settings", views.settings, name="settings"),
   path("loginn", views.loginn, name="loginn"),
   path("web", views.web, name="web"),
   path("data", views.data, name="data"),
   path("software", views.software, name="software"),
   path("video", views.video, name="video"),
   path('logoutt', views.logoutt, name='logoutt'),
   path('changepass', views.changepass, name='changepass'),
]
 