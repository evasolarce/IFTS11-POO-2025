


from django.db import models
import uuid

class Perro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    tamaño = models.CharField(max_length=50)
    peso = models.FloatField()
    estado_salud = models.CharField(max_length=100)
    vacunado = models.BooleanField(default=False)
    temperamento = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=[('disponible','Disponible'), ('reservado','Reservado'), ('adoptado','Adoptado')], default='disponible')


class UsuarioAdoptante(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    preferencias = models.JSONField(default=dict)  # {'raza': ..., 'edad': ..., 'tamaño': ...}
    historial_adopciones = models.ManyToManyField(Perro, blank=True, related_name='adoptantes')

    def __str__(self):
        return self.nombre
    
class SistemaAdopcion(models.Model):
        perros = models.ManyToManyField(Perro, blank=True)
        usuarios = models.ManyToManyField(UsuarioAdoptante, blank=True)

        def __str__(self):
            return "Sistema de Adopción"    
