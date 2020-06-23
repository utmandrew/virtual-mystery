from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('ta-viewset', views.ListPracticals, basename='ta-viewset')

urlpatterns = [
    url(r'^practicals/', views.ListPracticals.as_view()),
    url(r'^groups/(?P<praName>.*)', views.ListGroups.as_view()),
    url(r'^users/(?P<groupId>[0-9]*)', views.ListUsers.as_view()),
    # ^^ add a parameter
    url(r'^userCheck/', views.UserCheck.as_view()),
    url(r'^userComment/(?P<userName>.*)', views.UserComment.as_view()),

]
