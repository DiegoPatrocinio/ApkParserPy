from django.conf.urls import include, url
from django.conf import settings
from django.contrib.auth.models import User
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from backoffice import views


urlpatterns = [
    # Examples:
    url(r'^$', views.home, name='home'),

]