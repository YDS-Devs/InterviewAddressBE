from rest_framework import viewsets,mixins
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from .serializers import AddressSerializer, AreaSerializer, StateSerializer
from .models import Address, State,Area
from rest_framework.permissions import IsAuthenticated
# Create your views here 
class StateViewSet(ModelViewSet):
    queryset = State.objects.filter(country__name__icontains='Egypt')
    serializer_class = StateSerializer

class AreaViewSet(ModelViewSet):
    serializer_class = AreaSerializer
    def get_queryset(self):
        queryset = Area.objects.filter(state__id=self.kwargs.get('state_pk'))
        return queryset

    def get_serializer_context(self):
        return {'state_id':self.kwargs.get('state_pk')}

class AddressViewSet(ModelViewSet):
    
    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        queryset = Address.objects.filter(user=self.request.user)
        return queryset