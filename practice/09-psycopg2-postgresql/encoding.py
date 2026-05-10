import psycopg2

conn = psycopg2.connect(host = "localhost", database = "flis", user = "postgres", password = "Rounak@123", port = 5432)

cur = conn.cursor()
cur = conn.cursor()
cur.execute("select team_id from teams where jersey_home_color <> jersey_away_color order by team_id")

res = [i[0] for i in cur.fetchall()]
for i in res:
    for j in i:
        if j.isdigit():
            print(str((int(j)+7)%10), end="")
        else:
            print(chr((((ord(j.upper())-65) + 7)%26) + 65), end = "")
    print()



cur.close()
conn.close()