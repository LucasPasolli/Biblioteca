from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre=models.CharField(max_length=20)
    codigo=models.AutoField(primary_key=True)
    def __str__(self):
        return '{}'.format(self.nombre)



class Libro(models.Model):
    
    codigo = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 30)
    editorial = models.CharField(max_length = 30)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    paginas = models.IntegerField(default='1')
    def __str__(self):
        return str(self.titulo)



class Ejemplar(models.Model):
    localizacion=models.CharField(max_length=20)
    codigo=models.AutoField(primary_key=True)
    libro=models.ForeignKey(Libro, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.libro)


class Usuario(models.Model):
    nombre=models.CharField(max_length=20)
    telefono=models.IntegerField()
    direccion=models.CharField(max_length=20)
    codigo=models.AutoField(primary_key=True)
    ejemplares=models.ManyToManyField(Ejemplar)
    def __str__(self):
        return '{}'.format(self.nombre)


class Entry(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __unicode__(self):
        return '%s' % self.title

    def get_nombre(self):
        return self.autor.nombre
