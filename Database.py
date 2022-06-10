import sqlite3

# create A database
connection = sqlite3.connect('customer.db')

# creat a cursor
c = connection.cursor()

# query the database
c.execute("SELECT * FROM customers")

#fetchone()
#fetchmany(3)
print(c.fetchall())

print("command executed succesfully")

# commiting our database
connection.commit()

# close connection
connection.close()

