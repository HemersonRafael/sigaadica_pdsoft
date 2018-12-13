# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso
from .forms import CursoForm

def index(request):
    cursos = Curso.objects.all()
    return render(request, 'site/index.html', {'cursos': cursos})

def editar(request):
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