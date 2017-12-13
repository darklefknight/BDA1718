#!/bin/user/python
import numpy as np
import sys

class Geo(object):
    """
    Class containing the functions to get the closes points.
    """
    import googlemaps

    def __init__(self):
        """
        Initialising the class by opening a client to the google-API with my key
        """
        self.gmaps = self.googlemaps.Client(key='MyKey')

    def getLocations(self,place):
        """
        Get 10 random locations within 1000m of the input-location.
        :param place: String: A place somewhere on the earth
        :return:
        """
        geocode_result = self.gmaps.geocode(place) # get lat and lon of input
        lat = geocode_result[0]['geometry']['location']['lat']
        lon = geocode_result[0]['geometry']['location']['lng']

        ranger = np.linspace(0.99,1.01,1000)
        np.random.shuffle(ranger) # provide some randomness
        lats = np.multiply(lat,ranger) # some coordinates near the input
        lons = np.multiply(lon,ranger)

        dists = []
        points = []
        for lat1 in lats:
            for lon1 in lons:
                dist = self.getDistance(lat,lon,lat1,lon1) # calculate distance to input location

                if dist < 1000:
                    dists.append(dist)

                    # for a valid point get what google can find at this location:
                    geo_of_point = self.gmaps.reverse_geocode((lat1,lon1))
                    points.append(geo_of_point[0])

                if len(dists) >= 10:
                    break


        return points,dists


    @staticmethod
    def getDistance(lat1, lon1, lat2, lon2):
        """
        Calculating the closest distance between two coordinates using the harvesine formula
        """
        R = 6371e3  # Radiuas of earth in m
        phi1 = np.deg2rad(lat1)
        phi2 = np.deg2rad(lat2)

        delta_phi = np.deg2rad(lat2 - lat1)
        delta_lambda = np.deg2rad(lon2 - lon1)

        a = (np.sin(delta_phi / 2) ** 2) + (np.cos(phi1) * np.cos(phi2) * (np.sin(delta_lambda / 2) ** 2))
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
        d = R * c
        return d



if __name__ == "__main__":
    user_input = sys.argv[1] # sys.argv[0] is the own name of the script
    Gmap = Geo() # initialize class
    points,dists = Gmap.getLocations(user_input)

    for point,dist in zip(points,dists):
        print(point["formatted_address"] + ".      Distance to %s:%f7.3m"%(user_input,dist))
