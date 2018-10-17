from django.conf.urls import url
from . import views

app_name = 'comment'
urlpatterns = [
    url(r'^(?P<release>[0-9]*)$', views.CommentList.as_view(),
        name='comment_list'),
    url(r'^create$', views.CommentCreate.as_view(), name='comment_create'),
    url(r'^reply$', views.ReplyCreate.as_view(), name='reply_create'),
    url(r'^(?P<release>[0-9]*)/(?P<groupId>[0-9]*)$', views.TaCommentList.as_view(),name='ta_comment_list'),
    url(r'^resultCreate$', views.ResultCreate.as_view(), name='result_create'),


]
