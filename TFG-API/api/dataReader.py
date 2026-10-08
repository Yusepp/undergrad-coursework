# Libraries
import os
import pandas as pd
from os.path import isdir
from joblib import Parallel, delayed

# Django
from api.models import Weather, State, Part


class Reader():
    # "C:\Users\Yusepp\Desktop\datasets\722880-23152.csv"
    def __init__(self, directory):
        self.files = [directory+'/'+item for item in os.listdir(directory) if not isdir(item)]

        if len(self.files) >= 6:
            self.cores = 6
        else:
            self.cores = len(self.files)

    def read_weather_csv(self, file):
        csv = pd.read_csv(file)
        objs = [Weather(date=row.HR_TIME, lat=1.0, lon=1.0, temp=row.TEMP, max=row.MAX, min=row.MIN, dir=row.DIR,
                        prcp=row.PCP01) for row in csv.itertuples()]
        Weather.objects.bulk_create(objs)

    def read_all(self):
        try:
            for file in self.files:
                self.read_weather_csv(file)
            return "All objects created"

        except Exception as error:
            return error

    def read_icao_csv(self, file):
        csv = pd.read_csv(file)
        objs = [State(icao24=row.ICAO24, date=row.TIME, lat=row.LAT, lon=row.LON, onground=row.ONGROUND, baroalt=row.BAROALTITUDE,
                        geoalt=row.GEOALTITUDE, vel=row.VELOCITY, head=row.HEADING, vertsp=row.VERTSPEED) for row in csv.itertuples()]
        State.objects.bulk_create(objs)
        