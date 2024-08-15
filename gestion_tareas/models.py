from django.db import models
# Create your models here.

#MODELO GESTION DE TAREAS
class Tarea(models.Model):

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo