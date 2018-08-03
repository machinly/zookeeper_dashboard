from django.conf.urls import *
from zkadmin import views

urlpatterns = [
    url(r'^server/(?P<server_id>\d+)/$', views.detail), 
    url(r'^$',views.index), 
]
