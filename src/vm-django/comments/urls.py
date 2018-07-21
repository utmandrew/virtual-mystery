from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CommentList.as_view()),
    url(r'^create$', views.CommentCreate.as_view()),
    url(r'reply', views.ReplyCreate.as_view()),
]
