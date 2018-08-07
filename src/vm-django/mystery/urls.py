from django.conf.urls import url
from .views import ReleaseList

app_name = 'mystery'
urlpatterns = [
    url(r'^release/list$', ReleaseList.as_view(), name='release_list'),
]
