from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
	user = models.OneToOneField(User)
	def __unicode__(self):
		return  self.user

	class Meta:
		ordering = ['user']

class Departamento(models.Model):
	nombre= models.CharField(max_length=64,blank=True, null=True,)
	cabecera= models.CharField(max_length=64,blank=True, null=True,)
	idioma= models.CharField(max_length=64,blank=True, null=True,)
	def __unicode__(self):
		return  self.nombre

	class Meta:
		ordering = ['nombre']

class Municipio(models.Model):
	nombre= models.CharField(max_length=64,blank=True, null=True,)
	departamento= models.ForeignKey(Departamento, blank=True, null=True)
	def __unicode__(self):
		return  self.nombre
	class Meta:
		ordering = ['nombre']


class Habitacion(models.Model):
    numero= models.CharField(max_length=64,blank=True, null=True,)
    precio= models.CharField(max_length=64,blank=True, null=True,)
    CAPACIDAD_CHOICES = (
	(1, 'Individual'),
	(2, 'Doble'),
	(3, 'Triple'))
	
    CATEGORIA_CHOICES = (
	('Economico', 'Una'),
	('Estandar', 'Estandar'),
	('De Lujo', 'De Lujo'))
    capacidad= models.PositiveSmallIntegerField(blank=True, null=True,choices=CAPACIDAD_CHOICES)
    categoria= models.CharField(max_length=64,blank=True, null=True, choices=CATEGORIA_CHOICES)
    #disponible= models.BooleanField()


class Hotel(models.Model):
	ESTRELLAS_CHOICES = (
	(1, 'Una'),
	(2, 'Dos'),
	(3, 'Tres'),
	(4, 'Cuatro'),
	(5, 'Cinco'),
)
	nombre = models.CharField(max_length=64,blank=True, null=True,)
	direccion= models.CharField(max_length=64,blank=True, null=True,)
	telefono = models.CharField(max_length=64,blank=True, null=True,)
	municipio= models.ForeignKey(Municipio, blank=True, null=True)
	habitacion= models.ForeignKey(Habitacion,blank=True, null=True,)
	estrellas= models.IntegerField(blank=True, null=True, choices=ESTRELLAS_CHOICES)
	imagen= models.ImageField(upload_to='imghoteles')
	descripcion= models.TextField()
	def __unicode__(self):
		return  self.nombre

	class Meta:
		ordering = ['nombre', 'estrellas',]
		
class Reservacion(models.Model):
	user = models.ForeignKey(User, blank=True, null=True)
	llegada= models.DateField(blank=True, null=True)
	salida= models.DateField(blank=True, null=True)
	habitacion= models.ForeignKey(Habitacion,blank=True, null=True,)
	total=models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True,)
	
	def __unicode__(self):
		return  '{0} {1}'.format(self.hotel, self.salida)

	class Meta:
		ordering = ['salida']
