from django.conf.urls import url
from posts.views import *

urlpatterns = [
    url(r'^create/$', post_create, name="create"),
    url(r'^detail/(?P<post_slug>[-\w]+)/$',post_detail, name="detail"),
    url(r'^list/$', post_list, name="list"),
    url(r'^update/(?P<post_slug>[-\w]+)/$', post_update, name="update"),
    url(r'^delete/(?P<post_slug>[-\w]+)/$', post_delete, name="delete"),
]