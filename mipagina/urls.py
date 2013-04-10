from django.conf.urls import patterns, url
from mipagina import views

urlpatterns = patterns('',
    url(r'^$', views.solution), 
    #url(r'^contacto/(?P<num1>\d+)/(?P<num2>\d+)/(?P<opc>\d+)',views.calcula),
    url(r'^contacto/$',views.calcula),
    url(r'^contac/$',views.sol2),
)