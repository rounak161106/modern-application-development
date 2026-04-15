import psycopg2

conn = psycopg2.connect(database = "flis", user = "postgres", password = "Rounak@123", port = 5432, host = "localhost")
cur = conn.cursor()
cur.execute("Select jersey_no from players where name = '{}'".format("Shlok"))
print(cur.fetchone()[0])
