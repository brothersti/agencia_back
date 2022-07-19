from django.db import models

# Create your models here.


class Trayecto(models.Model):
    IdTrayecto = models.AutoField(primary_key=True)
    NombreTrayecto = models.CharField(max_length=200)
    Horario = models.DateTimeField()


class Bus(models.Model):
    IdBus = models.AutoField(primary_key=True)
    NumeroBus = models.CharField(max_length=10, unique=True)
    Capacidad = models.IntegerField()
    AsientoRestantes = models.IntegerField(default=None, blank=True, null=True)


class Chofer(models.Model):
    IdChofer = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    IdBus = models.ForeignKey(Bus,
                              null=True,
                              blank=True,
                              on_delete=models.CASCADE)
    IdTrayecto = models.ForeignKey(Trayecto,
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE)


class Pasajero(models.Model):
    IdPasajero = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Asiento = models.CharField(max_length=5, unique=True)
    IdBus = models.ForeignKey(Bus,
                              null=True,
                              blank=True,
                              on_delete=models.CASCADE)
    IdTrayecto = models.ForeignKey(Trayecto,
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE)
