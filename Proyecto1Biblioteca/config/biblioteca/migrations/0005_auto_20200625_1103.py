# Generated by Django 2.2 on 2020-06-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_auto_20200622_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='ejemplares',
        ),
        migrations.AddField(
            model_name='usuario',
            name='ejemplar',
            field=models.ManyToManyField(to='biblioteca.Ejemplar'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ejemplar',
            name='localizacion',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='libro',
            name='paginas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]