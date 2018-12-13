from home import views_geral
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views_geral.index, name = 'index'),
	url(r'^editar/$', views_geral.editar, name = 'editar'),
	#url(r'^(?P<atalho>[-\w]+)/$', views.search_estabelecimento, name='estabelecimento'),
	#url(r'^contato$', views.contato, name = 'contato'),
]
