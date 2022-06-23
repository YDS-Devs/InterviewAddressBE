from django.db import models


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
    # create new field called new char

    class Meta:
        db_table = 'address'
