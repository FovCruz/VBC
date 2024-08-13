from django.db import models

# Create your models here.
class Estudiante(models.Model):
    genero_opciones = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    ]

    rut = models.CharField('Rut del estudiante', max_length=50, primary_key=True)
    nombre = models.CharField('Nombre del estudiante', max_length=200)
    fecha_nac = models.DateField('Fecha de nacimiento', auto_now=False, auto_now_add=False)
    genero = models.CharField('Género', max_length=1, choices=genero_opciones)

    def __str__(self) -> str:
        return self.nombre