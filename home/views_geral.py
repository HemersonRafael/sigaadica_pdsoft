# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso
from .forms import CursoForm

def index(request):
    cursos = Curso.objects.all()
    return render(request, 'site/index.html', {'cursos': cursos})

def criar(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.save()
            #return redirect('detalhar', pk=curso.pk)
            return redirect('index')
    else:
        form = CursoForm()
    return render(request, 'site/editar.html', {'form': form})

def editar(request, pk):
    post = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            post = form.save(commit=False)
            post.nome = request.nome
            post.codigo = request.codigo
            post.ativo = request.ativo
            post.save()
            return redirect('detalhar', pk=post.pk)
    else:
        form = CursoForm(instance=post)
    return render(request, 'site/editar.html', {'form': form})

def detalhar(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'site/detalhar.html', {'curso': curso})

def remover(request, pk):
    Curso.objects.delete(pk=pk)
    return redirect('index')