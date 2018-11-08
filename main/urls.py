from django.conf.urls import url
from django.views.generic import * 
from main import views




urlpatterns = [
    url(r'^$', views.home, name='home'),



]