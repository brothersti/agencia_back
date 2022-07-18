from django import dispatch
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Bus, Chofer


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
        jsonData = json.loads(request.body)
        Bus.objects.create(NumeroBus=jsonData['NumeroBus'],
                           TotalAsientos=jsonData['TotalAsientos'])

        datos = {'message': "Succes"}
        return JsonResponse(datos)

# Metodo encargado de actualizar un bus
    def put(self, request, id):
        jsonData = json.loads(request.body)
        buses = list(Bus.objects.filter(IdBus=id).values())
        if len(buses) > 0:
            bus = Bus.objects.get(IdBus=id)
            bus.NumeroBus = jsonData['NumeroBus']
            bus.TotalAsientos = jsonData['TotalAsientos']
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
        jd = json.loads(request.body)
        Chofer.objects.create(Nombre=jd['Nombre'],
                              Apellido=jd['Apellido'],
                              IdBus= jd['IdBus'],
                              IdTrayecto= jd['IdTrayecto'])

        datos = {'message': "Succes"}
        return JsonResponse(datos)

# Metodo encargado de actualizar un chofer

    def put(self, request, id):
        jd = json.loads(request.body)
        choferes = list(Chofer.objects.filter(IdChofer=id).values())

        if len(choferes) > 0:
            chofer = Chofer.objects.get(IdChofer=id)
            chofer.Nombre = jd['Nombre']
            chofer.Apellido = jd['Apellido']
            chofer.IdBus = jd['IdBus']
            chofer.IdTrayecto = jd['IdTrayecto']
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
