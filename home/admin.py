from django.contrib import admin
from .models import Departamento, Curso

class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ['codigo', 'nome']
	search_fields = ['codigo']
	list_filter = ['nome']

class CursoAdmin(admin.ModelAdmin):
	list_display = ['codigo', 'nome', 'departamento', 'ativo']
	search_fields = ['codigo']
	list_filter = ['nome']
	
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Curso, CursoAdmin)