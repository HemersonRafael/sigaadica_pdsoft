# Generated by Django 2.1.3 on 2018-12-13 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='departamento',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Departamento', verbose_name='Departamento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turma',
            name='qnt_discentes',
            field=models.IntegerField(default=0, verbose_name='Quantidade de Discentes'),
            preserve_default=False,
        ),
    ]
