from rest_framework import viewsets,mixins
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from .serializers import AreaSerializer, StateSerializer
from .models import State,Area
# Create your views here 
class StateViewSet(ModelViewSet,GenericViewSet):
    queryset = State.objects.filter(country__name__icontains='Egypt')
    serializer_class = StateSerializer

class AreaViewSet(ModelViewSet,GenericViewSet):
    serializer_class = AreaSerializer
    def get_queryset(self):
        queryset = Area.objects.filter(state__id=self.kwargs.get('state_pk'))
        return queryset

    def get_serializer_context(self):
        return {'state_id':self.kwargs.get('state_pk')}