from django.db import models


# Create your models here.
class Bus(models.Model):
    IdBus = models.AutoField(primary_key=True)
    NumeroBus = models.CharField(max_length=10, unique=True)
    TotalAsientos = models.IntegerField()


class Chofer(models.Model):
    IdChofer = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    IdBus = models.IntegerField(unique=True)
    IdTrayecto = models.IntegerField()


class Pasajero(models.Model):
    IdPasajero = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Asiento = models.CharField(max_length=5, unique=True)
    IdBus = models.IntegerField()
    IdTrayecto = models.IntegerField()


class Trayecto(models.Model):
    IdTrayecto = models.AutoField(primary_key=True)
    NombreTrayecto = models.CharField(max_length=200)
    Horario = models.DateTimeField()
