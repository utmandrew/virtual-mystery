from django.conf.urls import url
from rest_framework.authtoken import views
from .views import Logout, Login, ChangePassword

app_name = 'authentication'
urlpatterns = [
    # url(r'^token$', views.obtain_auth_token, name="token"),
    url(r'^token$', Login.as_view(), name="token"),
    url(r'^logout$', Logout.as_view(), name="logout"),
    url(r'^changepassword$', ChangePassword.as_view(), name="changepassword"),
]
