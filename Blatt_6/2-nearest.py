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
    conn = psycopg2.connect("dbname=postgis")
    cur = conn.cursor()
    position = (53.1,10)
    citty_list = getPSQLatLoc(cur,position[0],position[1],0.1,10)

    cur.close()
    conn.close()
    print("Distance [m]   |   Place of interest")
    for tuple in citty_list:
        print("%7.4f     |    %s"%(tuple[0],tuple[1]) )