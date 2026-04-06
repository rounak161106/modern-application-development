import psycopg2

conn = psycopg2.connect(host = "localhost", database = "demo", user = "postgres", password = "Rounak@123", port = "5432")
print("Connection Successful!")

cur = conn.cursor()
# cur.execute("""Create table table3( id int primary key, name varchar(20), city varchar(20))""")
# print("Table created successfully!")

cur.execute("""Insert into table3 values(4, 'Rounak', 'Bangalore')""")
cur.execute("""Insert into table3 values(5, 'Rahul', 'Delhi')""")
cur.execute("""Insert into table3 values(6, 'Rohit', 'Mumbai')""")
print("Data inserted successfully!")
cur.execute("Select * from table3;")
result = cur.fetchall()

conn.commit()
cur.close()
conn.close()
print(result)   