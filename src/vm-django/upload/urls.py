from django.conf.urls import url
from . import views

app_name = 'upload'
urlpatterns = [
    url(r'^(?P<filename>.*)$', views.upload.as_view(), name='upload'),
]
