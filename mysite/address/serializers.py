from rest_framework import serializers
from .models import Address, State,Area

class StateSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):

        kwargs['country_id'] = 1 
        return super().save(**kwargs)
    class Meta:
        model = State
        fields = ('id','name','name_ar')

class AreaSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        kwargs['state_id'] = self.context['state_id']
        return super().save(**kwargs)
    class Meta:
        model = Area
        fields = ('id','name','name_ar')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id','area','name','description','floor_number','apartment_number','longitude','latitude')
    
    def save(self, **kwargs):
        self.validated_data['user'] = self.context['request'].user
        return super().save(**kwargs)

class ReadOnlyAddressSerializer(serializers.ModelSerializer):
    #serializer method to get area by name only
    area = serializers.CharField(source='area.name')
    state = serializers.CharField(source='area.state.name')


    class Meta:
        model = Address
        fields = ('area','state','description','longitude','latitude')
