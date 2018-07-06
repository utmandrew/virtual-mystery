from django.contrib import admin
from django.conf.urls import url
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^token$', views.obtain_auth_token),
]
