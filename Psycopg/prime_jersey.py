import psycopg2

conn = psycopg2.connect(host = "localhost", database = "flis", user = "postgres", password = "Rounak@123", port = 5432)

cur = conn.cursor()

cur.execute("Select * from players")
jer_nos = [i[3] for i in cur.fetchall()]
prime_jer = []
for i in jer_nos:
    ctr = 0
    for j in range(2, i//2+1):
        if i % j == 0:
            ctr += 1;
    if ctr == 0 and i != 1:
        prime_jer.append(i)


cur.execute("select players.name, teams.name from players join teams using (team_id) where jersey_no in {} order by players.name desc, teams.name desc;".format(tuple(prime_jer)))
res = cur.fetchall()

for i in res:
    print(i[0], i[1], sep=", ")
cur.close()
conn.close()