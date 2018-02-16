#coding:utf8
from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^post/(?P<id>\d+)/$',views.Detail,name="blog_detail"),
    url(r'^home/',views.home,name="blog_home"),
    url(r'^test/',views.Test,name="blog_test"),
    url(r'^list/',views.ListAll,name="blog_list"),
    url(r'^label/',views.LabelAll,name="blog_label"),
    url(r'^captain/',views.AboutMe,name="blog_about_me"),
    url(r'^advice/',views.userInfo,name="blog_advice"),
    url(r'',views.home,name="blog_home"),
]
