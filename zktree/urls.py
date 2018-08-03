from django.conf.urls import *
from zktree import views

urlpatterns = [
    url(r'^(?P<path>.*)/$',views.index), 
    url(r'^$',views.index), 
]
