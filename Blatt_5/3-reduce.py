#!/usr/bin/python3



##!/scratch/local1/m300517/anaconda3/bin/python3

import sys

class Weather:
    def __init__(self,liste):
        self.lat = liste[0]
        self.lon = liste[1]
        self.temp = liste[3]
        self.precip = liste[4]

    def append(self,liste):
        temp1 = float(liste[3])
        precip1 = float(liste[4])
        self.temp = str((float(self.temp) + temp1)/2)
        self.precip = str((float(self.precip) + precip1)/2)


class Location:
    def __init__(self,liste):
        self.lat = liste[0]
        self.lon = liste[1]
        self.names = []
        self.names.append(liste[2])

    def append(self,liste):
        self.names.append(liste[2])

def printOut(loc,wet):
    for name in loc.names:
        lat = loc.lat
        lon = loc.lon
        if float(loc.lat) > 180:
            lat = str(float(loc.lat) -360)
        if float(loc.lon) > 180:
            lon = str(float(loc.lon) -360)

        result_str = name + "," + lat + "," + lon + "," + wet[2] + "," + wet[3]
        print(result_str)

if __name__ == "__main__":
    location_list = []
    for line in sys.stdin:
        try: # if an empty line occurs, continue
            lineSplit = line.rstrip().split(",")
        except:
            continue

        lineType = None

        try:
            float(lineSplit[-1]) # when the last element is an integer, the line contains weather-data
            lineType = "weather"
        except:
            lineType = "name" # when the last element is an integer, the line contains the name of the location

        if lineType == "weather":
            if not "weather" in locals():
                weather = Weather(lineSplit)
                weather_sum = [weather.lat, weather.lon, weather.temp, weather.precip]

            if ((Weather(lineSplit).lat == weather.lat) and (Weather(lineSplit).lon == weather.lon)):
                weather.append(lineSplit)
                weather_sum = [weather.lat, weather.lon, weather.temp, weather.precip]

            else:
                weather_sum = [weather.lat,weather.lon,weather.temp,weather.precip]
                weather = Weather(lineSplit)


        elif lineType == "name":
            if not "location" in locals():
                location = Location(lineSplit)

            if ((Location(lineSplit).lat == location.lat) and (Location(lineSplit).lon == location.lon)):
                location.append(lineSplit)
            else:
                # if location.lat == weather_sum[0] and location.lon == weather_sum[1]:
                printOut(location,weather_sum)
                location = Location(lineSplit)

        else:
            continue

