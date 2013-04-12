from django.conf.urls import patterns, url
from mipagina import views

urlpatterns = patterns('',
    url(r'^$', views.formulario), 
    #url(r'^contacto/(?P<num1>\d+)/(?P<num2>\d+)/(?P<opc>\d+)',views.calcula),
    url(r'^contacto/$',views.formulario),
    url(r'^contac/$',views.sol2),
)