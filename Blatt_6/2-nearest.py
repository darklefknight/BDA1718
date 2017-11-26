#!/user/bin/python3

"""
This programm prints out the n closest points of interest for a user input.

The way it is done might not be the fastest or nicest, but since this should be a one hour task and it works it should
be sufficient.

In general what could be done better is the way the data is retrieved from the database. We get more data than we need
and afterwards deciding what we need from that.

By Finn Burgemeister and Tobias Machnitzki
"""
import psycopg2
import numpy as np


def getDistance(lat1,lon1,lat2,lon2):
    """
    Calculating the closest distance between two coordinates using the harvesine formula
    """
    R = 6371e3 # Radiuas of earth in m
    phi1 = np.deg2rad(lat1)
    phi2 = np.deg2rad(lat2)

    delta_phi = np.deg2rad(lat2-lat1)
    delta_lambda = np.deg2rad(lon2-lon1)

    a = (np.sin(delta_phi/2)**2) + (np.cos(phi1) * np.cos(phi2) * (np.sin(delta_lambda/2)**2))
    c = 2 * np.arctan2(np.sqrt(a),np.sqrt(1-a))
    d = R * c
    return d

def getPSQLatLoc(cur,lat,lon,distance,closest_n):
    """
    Gets a list of Titels around a location via psql. Afterwards reducing this list to "closest_n" elements.
    The result will be the closest_n elements to the entered location.
    """
    loc_list = []
    while len(loc_list) < closest_n+100:
        lat_low = lat - distance
        lat_high = lat + distance
        lon_low = lon - distance
        lon_high = lon + distance

        cur.execute('SELECT lat,lon,"Titel" FROM wp_coords_red0 WHERE lat BETWEEN {0} AND {1} AND lon BETWEEN {2} AND {3}'.format(lat_low,lat_high,lon_low,lon_high))
        loc_list = cur.fetchall()
        distance +=0.1

    dist_list = []
    for element in loc_list:
        dist = getDistance(lat,lon,element[0],element[1])
        dist_list.append((dist,element[2]))

    return sorted(dist_list)[:closest_n]

if __name__ == "__main__":
    # Gettin the User input:
    in_text = "Please enter your position. First latitude then longitude,seperated by comma. \n Example: 52.025,10.113 \n"
    lat,lon = tuple(float(x.strip()) for x in input(in_text).split(','))
    results = int(input("How many results do you want to get?\n"))
    position = (lat,lon)

    #creating psql connection:
    conn = psycopg2.connect("dbname=postgis")
    cur = conn.cursor()

    # from user input get closest elements:
    citty_list = getPSQLatLoc(cur,position[0],position[1],0.1,results)

    #close connection:
    cur.close()
    conn.close()

    # output results:
    print("Distance [m]   |   Place of interest")
    for tuple in citty_list:
        print("%09.5f     |    %s"%(tuple[0],tuple[1]) )