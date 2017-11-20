#!/usr/bin/python3


##!/scratch/local1/m300517/anaconda3/bin/python3

import sys

class Netcdf:
    def __init__(self,liste):
        self.date = liste[0]
        self.lat = liste[1]
        self.lon = liste[2]
        self.temp = liste[3]
        self.precip = liste[4]
        self.key = self.__getKey()

    def __str__(self):
        """
        lat and lon dont need to be in the return string as they are implemented in the key
        :return: str
        """
        return (self.key + "," + self.date + "," + self.temp + "," + self.precip)

    def __getKey(self):
        __lat = float(self.lat)
        __lon = float(self.lon)

        __lat = (round(__lat, 2))
        __lon = (round(__lon, 2))

        # to avoid negative keys:
        if __lat < 0 : __lat += 360
        if __lon < 0 : __lon += 360

        __lat = "%07.2f"%__lat
        __lon = "%07.2f"%__lon

        return __lat+ "," +__lon


class Coordinates:
    def __init__(self,liste):
        self.name = liste[0]
        self.lat = liste[1]
        self.lon = liste[2]
        self.key = self.__getKey()

    def __str__(self):
        return (self.key + "," + self.name)

    def __getKey(self):
        __lat = float(self.lat)
        __lon = float(self.lon)

        __lat = (round(__lat, 2))
        __lon = (round(__lon, 2))

        # to avoid negative keys:
        if __lat < 0 : __lat += 360
        if __lon < 0 : __lon += 360

        __lat = "%07.2f"%__lat
        __lon = "%07.2f"%__lon

        return __lat+ "," +__lon

def main():
    for line in sys.stdin:
        try:

            lineSplit = line.rstrip().split(",")
        except:
            continue

        if len(lineSplit) == 5: # The netcdf file has 5 columns
            try:
                float(lineSplit[1]) # if header, than go to next loop
            except:
                continue

            print(Netcdf(lineSplit))

        elif len(lineSplit) == 3: # the wiki-coordinates file has only 3 columns
            try:
                float(lineSplit[1]) # if header, than go to next loop
            except:
                continue

            print(Coordinates(lineSplit))


if __name__ == "__main__":
    main()
