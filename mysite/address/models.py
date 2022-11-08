from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()

class Country(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    name_ar = models.CharField(max_length=255)

    class Meta:
        db_table = 'country'


class State(models.Model):
    country = models.ForeignKey(
        Country, null=False, blank=False, on_delete=models.deletion.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    name_ar = models.CharField(max_length=255)

    class Meta:
        db_table = 'state'


class Area(models.Model):
    state = models.ForeignKey(
        State, null=False, blank=False, on_delete=models.deletion.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    name_ar = models.CharField(max_length=255)

    class Meta:
        db_table = 'area'

    def __str__(self) -> str:
        return self.name



class Address(models.Model):

    area = models.ForeignKey(
        Area, null=False, blank=False, on_delete=models.deletion.CASCADE)
    description = models.TextField(null=False, blank=False)

    name = models.CharField(max_length=255, null=False, blank=False)
    floor_number = models.IntegerField(null=False, blank=False)
    apartment_number = models.IntegerField(null=False, blank=False)
    longitude = models.DecimalField("Longitude", max_digits=9, decimal_places=6,null=False, blank=False)
    latitude = models.DecimalField("Latitude", max_digits=9, decimal_places=6,null=False, blank=False)
    user = models.ForeignKey(USER,on_delete=models.deletion.CASCADE,related_name='addresses')

    def __str__(self) -> str:
        return self.name
        
    class Meta:
        db_table = 'address'