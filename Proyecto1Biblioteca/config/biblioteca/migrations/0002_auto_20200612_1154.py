# Generated by Django 2.2 on 2020-06-12 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ejemplar',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='paginas',
        ),
        migrations.AddField(
            model_name='usuario',
            name='ejemplares',
            field=models.ManyToManyField(to='biblioteca.Ejemplar'),
        ),
    ]
