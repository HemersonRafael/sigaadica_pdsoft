"""sigaadica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from home.views import ProfessorViewSet
from home.views import DepartamentoViewSet 
from home.views import CursoViewSet
from home.views import DisciplinaViewSet
from home.views import TurmaViewSet
from home.views import AvaliacaoViewSet

router = routers.DefaultRouter()
router.register(r'professores', ProfessorViewSet)
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'disciplinas', DisciplinaViewSet)
router.register(r'turmas', TurmaViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
