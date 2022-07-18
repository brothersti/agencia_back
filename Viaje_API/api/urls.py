from django.urls import  path
from api.views import ChoferesView
from api.views import BusesView

urlpatterns = [
    path('buses/', BusesView.as_view(), name='buses_list'),
    path('buses/<int:id>', BusesView.as_view(), name='buses_process'),
    path('choferes/', ChoferesView.as_view(), name='choferes_list'),
    path('choferes/<int:id>', ChoferesView.as_view(), name='choferes_process')
]