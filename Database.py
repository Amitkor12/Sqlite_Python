import sqlite3

# create A database
connection = sqlite3.connect('customer.db')

# creat a cursor
c = connection.cursor()

# create a table
c.execute("""CREATE TABLE customers(
    first_name text,
    last_name text,
    email text
)
""")

# commiting our database
connection.commit()

# close connection
connection.close()

