from ast import Try
from dataclasses import fields
from tkinter import FLAT
from django import dispatch
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import json

from pyodbc import Error

from .models import Bus, Chofer, Pasajero, Trayecto
from .serializes import BusWithoutChofer


# Create your views here.
class BusesView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# Metodo encargado de obterne todos los buses o un bus por el id

    def get(self, request, id=0):
        if (id > 0):
            buses = list(Bus.objects.filter(IdBus=id).values())
            if len(buses) > 0:
                bus = buses[0]
                datos = {'message': "Succes", 'bus': bus}
            else:
                datos = {'message': "Not found..."}
            return JsonResponse(datos)
        else:
            buses = list(Bus.objects.values())
            if len(buses) > 0:
                datos = {'message': "Succes", 'buses': buses}
            else:
                datos = {'message': "Not found..."}
            return JsonResponse(datos)

# Metodo encargado de agregar un bus

    def post(self, request):
        try:
            jsonData = json.loads(request.body)
            Bus.objects.create(NumeroBus=jsonData['NumeroBus'],
                               Capacidad=jsonData['Capacidad'],
                               AsientoRestantes=jsonData['AsientoRestantes'])

            datos = {'message': "Succes"}
        except Error as ex:
            datos = ex

        return JsonResponse(datos)

# Metodo encargado de actualizar un bus

    def put(self, request, id):
        jsonData = json.loads(request.body)
        buses = list(Bus.objects.filter(IdBus=id).values())
        if len(buses) > 0:
            bus = Bus.objects.get(IdBus=id)
            bus.NumeroBus = jsonData['NumeroBus']
            bus.Capacidad = jsonData['Capacidad']
            bus.AsientosRestantes = jsonData['AsientosRestantes']
            bus.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Not found..."}
        return JsonResponse(datos)


# Metodo encargado de eliminar un bus

    def delete(self, request, id):
        buses = list(Bus.objects.filter(IdBus=id).values())
        if len(buses) > 0:
            Bus.objects.filter(IdBus=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Not found..."}
        return JsonResponse(datos)


class ChoferesView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# Metodo encargado de obterne todos los buses o un bus por el id

    def get(self, request, id=0):
        if (id > 0):
            choferes = list(Chofer.objects.filter(IdChofer=id).values())
            if len(choferes) > 0:
                chofer = choferes[0]
                datos = {'message': "Succes", 'chofer': chofer}
            else:
                datos = {'message': "Not found..."}
            return JsonResponse(datos)
        else:
            choferes = list(Chofer.objects.values())
            if len(choferes) > 0:
                datos = {'message': "Succes", 'choferes': choferes}
            else:
                datos = {'message': "Not found..."}
            return JsonResponse(datos)

# Metodo encargado de agregar un chofer

    def post(self, request):
        try:
            jd = json.loads(request.body)
            Chofer.objects.create(Nombre=jd['Nombre'],
                                  Apellido=jd['Apellido'],
                                  IdBus_id=jd['IdBus_id'],
                                  IdTrayecto_id=jd['IdTrayecto_id'])

            datos = {'message': "Succes"}
        except Error as ex:
            datos = ex

        return JsonResponse(datos)
# Metodo encargado de actualizar un chofer

    def put(self, request, id):
        jd = json.loads(request.body)
        choferes = list(Chofer.objects.filter(IdChofer=id).values())

        if len(choferes) > 0:
            chofer = Chofer.objects.get(IdChofer=id)
            chofer.Nombre = jd['Nombre']
            chofer.Apellido = jd['Apellido']
            chofer.IdBus = jd['IdBus_id']
            chofer.IdTrayecto = jd['IdTrayecto_id']
            chofer.save()

            datos = {'message': "Success"}
        else:
            datos = {'message': "Not found..."}
        return JsonResponse(datos)


# Metodo encargado de eliminar un bus

    def delete(self, request, id):
        choferes = list(Chofer.objects.filter(IdChofer=id).values())
        if len(choferes) > 0:
            Chofer.objects.filter(IdChofer=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Not found..."}
        return JsonResponse(datos)


class TrayectosView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# Metodo encargado de obterne todos los trayectos

    def get(self, request, id=0):
        if (id > 0):
            trayectos = list(Trayecto.objects.filter(IdTrayecto=id).values())
            if len(trayectos) > 0:
                trayecto = trayectos[0]
                datos = {'message': "Succes", 'trayecto': trayecto}
            else:
                datos = {'message': "Not found..."}
            return JsonResponse(datos)
        else:
            trayectos = list(Trayecto.objects.values())
            if len(trayectos) > 0:
                datos = {'message': "Succes", 'trayectos': trayectos}
            else:
                datos = {'message': "Not found..."}
            return JsonResponse(datos)

# Metodo encargado de agregar un trayecto

    def post(self, request):
        try:
            jd = json.loads(request.body)
            Trayecto.objects.create(NombreTrayecto=jd['NombreTrayecto'],
                                    Horario=jd['Horario'])
            datos = {'message': "Succes"}
        except Error as ex:
            datos = ex

        return JsonResponse(datos)

# Metodo encargado de actualizar un trayecto

    def put(self, request, id):
        jd = json.loads(request.body)
        trayectos = list(Trayecto.objects.filter(IdTrayecto=id).values())

        if len(trayectos) > 0:
            trayecto = Trayecto.objects.get(IdTrayecto=id)
            trayecto.NombreTrayecto = jd['NombreTrayecto']
            trayecto.Horario = jd['Horario']
            trayecto.save()

            datos = {'message': "Success"}
        else:
            datos = {'message': "Not found..."}
        return JsonResponse(datos)


# Metodo encargado de eliminar un trayecto

    def delete(self, request, id):
        trayecto = list(Chofer.objects.filter(IdTrayecto=id).values())
        if len(trayecto) > 0:
            Trayecto.objects.filter(IdTrayecto=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Not found..."}
        return JsonResponse(datos)


class PasajerosView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

# Metodo encargado de obterne todos los buses o un bus por el id

    def get(self, request, id=0):
        if (id > 0):
            pasajeros = list(Pasajero.objects.filter(IdPasajero=id).values())
            if len(pasajeros) > 0:
                pasajero = pasajeros[0]
                datos = {'message': "Succes", 'pasajero': pasajero}
            else:
                datos = {'message': "Not found..."}
            return JsonResponse(datos)
        else:
            pasajeros = list(Pasajero.objects.values())
            if len(pasajeros) > 0:
                datos = {'message': "Succes", 'pasajeros': pasajeros}
            else:
                datos = {'message': "Not found..."}
            return JsonResponse(datos)

# Metodo encargado de agregar un chofer

    def post(self, request):
        try:
            jd = json.loads(request.body)
            Pasajero.objects.create(Nombre=jd['Nombre'],
                                    Asiento=jd['Asiento'],
                                    IdBus_id=jd['IdBus_id'],
                                    IdTrayecto_id=jd['IdTrayecto_id'])            
           
            datos = {'message': "Succes"}

        except Error as ex:
            datos = ex

        return JsonResponse(datos)

# Metodo encargado de actualizar un chofer

    def put(self, request, id):
        jd = json.loads(request.body)
        pasajeros = list(Pasajero.objects.filter(IdPasajero=id).values())

        if len(pasajeros) > 0:
            pasajero = Pasajero.objects.get(IdPasajero=id)
            pasajero.Nombre = jd['Nombre']
            pasajero.Asiento = jd['Asiento']
            pasajero.IdBus = jd['IdBus']
            pasajero.IdTrayecto = jd['IdTrayecto']
            pasajero.save()

            datos = {'message': "Success"}
        else:
            datos = {'message': "Not found..."}
        return JsonResponse(datos)


# Metodo encargado de eliminar un bus

    def delete(self, request, id):
        pasajeros = list(Pasajero.objects.filter(IdPasajero=id).values())
        if len(pasajeros) > 0:
            Pasajero.objects.filter(IdPasajero=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Not found..."}
        return JsonResponse(datos)


class ChoferBusView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# Metodo encargado de obterne todos los buses o un bus por el id

    def get(self, request):
        query = 'SELECT "IdBus", "NumeroBus" FROM api_bus '\
                'WHERE "IdBus" NOT IN(select "IdBus_id" from api_chofer)'
        res = BusWithoutChofer(Bus.objects.raw(query), many=True).data
       
        datos = {'message': "Succes", 'buses': res}
        return JsonResponse(datos)
