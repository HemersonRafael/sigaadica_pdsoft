from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import ProfessorSerializer, DepartamentoSerializer, CursoSerializer, DisciplinaSerializer, TurmaSerializer, AvaliacaoSerializer
from .models import Professor, Departamento, Curso, Disciplina, Turma, Avaliacao

class ProfessorViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Professor.
    """
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.all() 

class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Departamentos.
    """
    serializer_class = DepartamentoSerializer
    queryset = Departamento.objects.all() 

class CursoViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Curso.
    """
    serializer_class = CursoSerializer
    queryset = Curso.objects.all() 
    
class DisciplinaViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Disciplina.
    """
    serializer_class = DisciplinaSerializer
    queryset = Disciplina.objects.all() 

class TurmaViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Turma.
    """
    serializer_class = TurmaSerializer
    queryset = Turma.objects.all() 

class AvaliacaoViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Avaliacao.
    """
    serializer_class = AvaliacaoSerializer
    queryset = Avaliacao.objects.all()