import psycopg2


def getPSQLatLoc(cur,lat,lon,distance):
    lat_low = lat - distance
    lat_high = lat + distance
    lon_low = lon - distance
    lon_high = lon + distance
    cur.execute('SELECT lat,lon,"Titel" FROM wp_coords_red0 WHERE lat BETWEEN {0} AND {1} AND lon BETWEEN {2} AND {3}'.format(lat_low,lat_high,lon_low,lon_high))
    loc_list = cur.fetchall()
    return loc_list

if __name__ == "__main__":
    conn = psycopg2.connect("dbname=postgis")
    cur = conn.cursor()
    citty_list = getPSQLatLoc(cur,52.1,10,0.1)

    cur.close()
    conn.close()
    print(citty_list)