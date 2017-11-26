import psycopg2


def getPSQLatLoc(cur,lat,lon,distance,closest_n):
    while len(loc_list) < closest_n:
        lat_low = lat - distance
        lat_high = lat + distance
        lon_low = lon - distance
        lon_high = lon + distance

        cur.execute('SELECT lat,lon,"Titel" FROM wp_coords_red0 WHERE lat BETWEEN {0} AND {1} AND lon BETWEEN {2} AND {3}'.format(lat_low,lat_high,lon_low,lon_high))
        loc_list = cur.fetchall()
        distance +=0.01


    return loc_list

if __name__ == "__main__":
    conn = psycopg2.connect("dbname=postgis")
    cur = conn.cursor()
    citty_list = getPSQLatLoc(cur,52.1,10,0.01,10)

    cur.close()
    conn.close()
    for tuple in citty_list:
        print("%7.4f | %7.4f | %s"%(tuple[0],tuple[1],tuple[2]) )