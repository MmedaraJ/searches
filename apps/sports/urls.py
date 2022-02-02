from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^search$', views.search, name='search'),
    url(r'^find$', views.find, name='find'),
    url(r'^filter$', views.filter, name='filter')
]