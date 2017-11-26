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
    in_text = "Please enter your position. First latitude then longitude,seperated by comma. \n Example: 52.025,10.113 \n"

    lat,lon = tuple(float(x.strip()) for x in input(in_text).split(','))
    print(lat,lon)
    results = input("How many results do you want to get?\n")
    conn = psycopg2.connect("dbname=postgis")
    cur = conn.cursor()
    position = (lat,lon)
    citty_list = getPSQLatLoc(cur,position[0],position[1],0.1,results)

    cur.close()
    conn.close()
    print("Distance [m]   |   Place of interest")
    for tuple in citty_list:
        print("%09.5f     |    %s"%(tuple[0],tuple[1]) )