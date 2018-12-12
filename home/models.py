from django.db import models

class Professor(models.Model):
    
    codigo = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)    
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering = ('nome', 'codigo')


class Departamento(models.Model):
    codigo = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)    
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ('nome', 'codigo')


class Curso(models.Model):
    departamento = models.ForeignKey(
        Departamento, 
        verbose_name='Departamento', 
        on_delete=models.CASCADE
    )
    codigo = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)    
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ('departamento','nome', 'codigo')


class Disciplina(models.Model):
    departamento = models.ForeignKey(
        Departamento, 
        verbose_name='Departamento', 
        on_delete=models.CASCADE
    )
    codigo = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)    
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ('departamento', 'nome', 'codigo',)

class Turma(models.Model):
    professor = models.ForeignKey(
        Professor, 
        verbose_name='Professor', 
        on_delete=models.CASCADE
    )
    disciplina = models.ForeignKey(
        Disciplina, 
        verbose_name='Disciplina', 
        on_delete=models.CASCADE
    )
    codigo = models.CharField(max_length=100)
    qnt_discentes = models.IntegerField()
    tx_aprov = models.FloatField()
    media_turma = models.FloatField()
    qnt_tranc = models.IntegerField()
    aprov_prim = models.IntegerField()
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{} - {}'.format(self.codigo, self.disciplina)
    
    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ('professor','disciplina', 'codigo',)

class Avaliacao(models.Model):
    turma = models.ForeignKey(
        Turma, 
        verbose_name='Turma', 
        on_delete=models.CASCADE
    )
    codigo = models.CharField(max_length=100)
    auto_avaliacao = models.FloatField() 
    post_prof = models.FloatField()
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.codigo, self.turma)
    
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ('turma','codigo', 'turma',)


