from django.conf.urls import url
from django.contrib import admin
from . import views

handler404 = 'website.views.handler404'

urlpatterns = [
	url(r'^$', views.home, name="home"),
	url(r'login', views.login, name="login")
]
