from django.conf.urls import url
from posts.views import *

urlpatterns = [
    url(r'^create/$', post_create, name="create"),
    url(r'^detail/(?P<post_id>\d+)/$',post_detail, name="detail"),
    url(r'^list/$', post_list, name="list"),
    url(r'^update/$', post_update, name="update"),
    url(r'^delete/$', post_delete, name="delete"),
]