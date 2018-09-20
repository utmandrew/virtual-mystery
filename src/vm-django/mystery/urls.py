from django.conf.urls import url
from .views import ReleaseList, ArtifactView

app_name = 'mystery'
urlpatterns = [
    url(r'^release/list$', ReleaseList.as_view(), name='release_list'),
    url(r'release/(?P<release>[0-9]*)$', ArtifactView.as_view(),
        name='artifact_view'),
]
