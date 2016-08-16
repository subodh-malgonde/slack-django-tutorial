from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^slack/oauth/$', views.slack_oauth),
]