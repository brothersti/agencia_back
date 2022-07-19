from django.urls import  path
from api.views import ChoferesView
from api.views import BusesView
from api.views import TrayectosView
from api.views import PasajerosView
from api.views import ChoferBusView

urlpatterns = [
    path('buses/', BusesView.as_view(), name='buses_list'),
    path('buses/<int:id>', BusesView.as_view(), name='buses_process'),
    path('choferes/', ChoferesView.as_view(), name='choferes_list'),
    path('choferes/<int:id>', ChoferesView.as_view(), name='choferes_process'),
    path('trayectos/', TrayectosView.as_view(), name='trayectos_list'),
    path('trayectos/<int:id>', TrayectosView.as_view(), name='trayectos_process'),
    path('pasajeros/', PasajerosView.as_view(), name='pasajeros_list'),
    path('pasajeros/<int:id>', PasajerosView.as_view(), name='pasajeros_process'),
    path('busChofer/', ChoferBusView.as_view(), name='busChofer_process')
]