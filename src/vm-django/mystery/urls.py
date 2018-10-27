from django.conf.urls import url
from .views import ReleaseList, Artifact, GroupsRelaseList

app_name = 'mystery'
urlpatterns = [
    url(r'^release/list$', ReleaseList.as_view(), name='release_list'),
    url(r'release/(?P<release>[0-9]*)$', Artifact.as_view(),
        name='artifact_view'),
    url(r'release/group/(?P<groupId>[0-9]*)$', GroupsRelaseList.as_view(),
        name='groups_relases'),
]
