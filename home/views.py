from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

### CURSOS ###

@api_view(['GET'])
def curso(request):
    """
    View responsável por exibir todos os cursos
    """
    cursos_serializer = CursoSerializer(Curso.objects.all(), many=True)
    return Response(cursos_serializer.data)


@api_view(['GET'])
def curso_id(request, id):
    """
    View responsável por devolver um curso específico pelo seu id
    """
    try:
        curso = Curso.objects.get(id=id)
        curso_serialzer = CursoSerializer(curso)

        return Response(curso_serialzer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def curso_por_departamento(request, id):
    """
    View responsável por pegar todos os cursos de um determinado departamento
    """
    pass