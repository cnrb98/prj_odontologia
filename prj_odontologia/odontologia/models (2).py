from django.db import models
from datetime import datetime

DIA_CHOICE = (
    ('L', 'Lunes'),
    ('M', 'Martes')
)

class Localidad(models.Model):
    nombre = models.CharField(max_length=50)
    cp = models.IntegerField("Código Postal")

    class Meta:
        verbose_name_plural = 'Localidades'

    def __str__(self):
        return '%s - %s' % (self.nombre, self.cp)


class Persona(models.Model):
    num_doc = models.CharField("Nº de documento", max_length=20, primary_key=True)
    nombre = models.CharField("Nombre/s", max_length=150)
    apellido = models.CharField(max_length=150)
    num_cuit = models.CharField("Nº de CUIT/CUIL", max_length=20, null=True, blank=True)
    fecha_nac = models.DateField("Fecha de nacimiento", default=datetime.now)
    telefono = models.CharField("Nº de teléfono", max_length=50, null=True, blank=True)
    email = models.EmailField("E-mail", null=True, blank=True)
    direccion = models.CharField(max_length=120)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, related_name='persona_localidad')

    class Meta:
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return '%s, %s' % (self.apellido, self.nombre)

# class Calendario(models.Model):
#     dia = models.CharField("Dia de la semana", max_length=1, choices=DIA_CHOICE, default='L')
#     hora = models.DateTimeField
#
# class Profesional(models.Model):
#     persona = models.ForeignKey(Persona)

