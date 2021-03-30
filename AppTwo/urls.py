from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    url('', views.users, name="users"),
    url('', views.help, name="help"),
    url('', views.index, name="index"),
]
