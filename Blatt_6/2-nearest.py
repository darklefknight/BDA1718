import psycopg2

if __name__ == "__main__":
    conn = psycopg2.connect("dbname=postgis")
    cur = conn.cursor()
    cur.execute("SELECT * FROM CITIES LIMIT 10;")
    citty_list = cur.fetchall()
    for element in citty_list:
        print(element)