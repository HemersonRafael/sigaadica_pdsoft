from home import views_geral
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views_geral.index, name = 'index'),
	url(r'^criar/$', views_geral.criar, name = 'criar'),
	url(r'^editar/(?P<pk>[0-9]+)/$', views_geral.editar, name = 'editar'),
	url(r'^(?P<pk>[-\w]+)/$', views_geral.detalhar, name = 'detalhar'),
]
