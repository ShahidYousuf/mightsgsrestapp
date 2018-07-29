#from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'mgsapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^go/$', views.go, name='go'),
]