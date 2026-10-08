from django.db import models
from tfgApi import settings


class Part(models.Model):
    PN = models.FloatField(blank=False)
    ATA = models.FloatField(blank=False)
    name = models.CharField(blank=False, max_length=1000)

class Aircraft(models.Model):
    icao24 = models.CharField(blank=False, max_length=15)
    regnum = models.CharField(blank=False, max_length=15)
    borndate = models.DateField(blank=True)
    actyp = models.CharField(blank=False, max_length=15)


class Flight_Hrs(models.Model):
    aircarft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    recorddate = models.DateField(blank=False, max_length=15)
    flyhours = models.FloatField(blank=False)
    ldgs = models.FloatField(blank=True)


class Defect(models.Model):
    PN = models.ForeignKey(Part, models.CASCADE)
    SN = models.CharField(blank=True, max_length=50)
    TSN = models.FloatField(blank=True)
    description = models.CharField(blank=True, max_length=1500)
    defdate = models.DateField(blank=False)
    airframehrs = models.FloatField(blank=False)
    defcode = models.FloatField(blank=True, max_length=10)

class Weather(models.Model):
    date = models.DateTimeField(blank=False)
    lat = models.FloatField(blank=False)
    lon = models.FloatField(blank=False)
    temp = models.FloatField(blank=True)
    max = models.FloatField(blank=True)
    min = models.FloatField(blank=True)
    dir = models.FloatField(blank=True)
    prcp = models.FloatField(blank=True)

class State(models.Model):
    icao24 = models.CharField(blank=False, max_length=15)
    date = models.DateTimeField(blank=False)
    lat = models.FloatField(blank=False)
    lon = models.FloatField(blank=False)
    head = models.FloatField(blank=False)
    vel = models.FloatField(blank=False)
    vertsp = models.FloatField(blank=False)
    onground = models.BooleanField(blank=False)
    baroalt = models.FloatField(blank=False)
    geoalt = models.FloatField(blank=False)