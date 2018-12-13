# Generated by Django 2.1.3 on 2018-12-13 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('auto_avaliacao', models.FloatField()),
                ('post_prof', models.FloatField()),
                ('ativo', models.BooleanField(default=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
                'ordering': ('turma', 'codigo', 'turma'),
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('ativo', models.BooleanField(default=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ('departamento', 'nome', 'codigo'),
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('ativo', models.BooleanField(default=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'ordering': ('nome', 'codigo'),
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('ativo', models.BooleanField(default=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Departamento', verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
                'ordering': ('departamento', 'nome', 'codigo'),
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('ativo', models.BooleanField(default=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
                'ordering': ('nome', 'codigo'),
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('qnt_discentes', models.IntegerField()),
                ('tx_aprov', models.FloatField()),
                ('media_turma', models.FloatField()),
                ('qnt_tranc', models.IntegerField()),
                ('aprov_prim', models.IntegerField()),
                ('ativo', models.BooleanField(default=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Disciplina', verbose_name='Disciplina')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Professor', verbose_name='Professor')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
                'ordering': ('professor', 'disciplina', 'codigo'),
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Departamento', verbose_name='Departamento'),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Turma', verbose_name='Turma'),
        ),
    ]
