"""
intro.py — Psycopg2: Connecting to PostgreSQL from Python
==========================================================
Practice: Working with PostgreSQL directly (beyond SQLite)

This was my exploration of connecting to a real PostgreSQL database
from Python using the psycopg2 library. Unlike SQLite (which is file-based),
PostgreSQL is a full client-server database system.

The workflow for psycopg2 is:
    1. Create connection (connect to the database server)
    2. Create cursor (interface for executing queries)
    3. Execute the query
    4. Commit or rollback the transaction
    5. Close the cursor
    6. Close the connection

This was beyond the course syllabus — I explored it out of curiosity
to understand how real-world database connections work.

Note: Database credentials are hardcoded here for learning purposes.
      In production, always use environment variables!

Key concepts learned:
    - psycopg2.connect() for establishing PostgreSQL connections
    - Cursor objects for executing SQL queries
    - fetchall() to retrieve query results
    - Proper resource cleanup (closing cursor and connection)
    - Error handling with try/except for database operations
"""

# create connection
# create cursor
# execute the query
# commit / rollback
# close the cursor 
# close the connection

import psycopg2

try:
    # Establish connection to the PostgreSQL server
    conn = psycopg2.connect(
        host="localhost",
        database="flis",
        user="postgres",
        password="Rounak@123",
        port="5432"   # default PostgreSQL port
    )

    print("Connected successfully!")

    # Create a cursor object to execute queries
    cur = conn.cursor()

    # Example query — fetch all rows from the players table
    cur.execute("SELECT * from players;")
    result = cur.fetchall()
    print(result)

    # Always close cursor and connection when done
    cur.close()
    conn.close()

except Exception as e:
    print("Error: 😭", e)