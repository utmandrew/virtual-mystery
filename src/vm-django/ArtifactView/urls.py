from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.ArtifactViewData, base_name='hello-viewset')

urlpatterns = [
    url(r'^artifact-view/', views.ArtifactViewData.as_view()),
    #url(r'', include(router.urls))
]
