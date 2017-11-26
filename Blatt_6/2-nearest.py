import psycopg2


def getPSQLatLoc(cur,lat,lon,distance):
    lat_low = lat - distance
    lat_high = lat + distance
    lon_low = lon - distance
    lon_high = lon + distance
    cur.execute("SELECT lat,lon FROM wp_coords_red0 WHERE {0}<lat AND lat<{1} AND {2}<lon AND lon<{3}".format(lat_low,lat_high,lon_low,lon_high))
    loc_list = cur.fetchall()
    return loc_list

if __name__ == "__main__":
    conn = psycopg2.connect("dbname=postgis")
    cur = conn.cursor()
    citty_list = getPSQLatLoc(cur,53,13,2)
    for element in citty_list:
        print(element)