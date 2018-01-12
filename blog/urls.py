from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]




'''
pk-matches the name we gave the primary key variable back in 
blog/templates/blog/post_list.html
'''
