from django.conf.urls import url

from . import views

urlpatterns = [
      url(r'^registrar/$', views.registrar ),
      url (r'^$', views.registrar, name = 'registro'),
      url(r'^crear_usuario/$', views.crear_usuario, name = 'crear_usuario'),
      url(r'^iniciosesion/$', views.iniciosesion, name = 'iniciosesion')

      ]
