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
