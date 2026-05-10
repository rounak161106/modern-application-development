# create connection
# create cursor
# execute the query
# commit / rollback
# close the cursor 
# close the connection

import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="flis",
        user="postgres",
        password="Rounak@123",
        port="5432"   # default PostgreSQL port
    )

    print("Connected successfully!")

    cur = conn.cursor()

    # Example query
    cur.execute("SELECT * from players;")
    result = cur.fetchall()
    print(result)

    cur.close()
    conn.close()

except Exception as e:
    print("Error: 😭", e)