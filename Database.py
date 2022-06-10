import sqlite3

# create A database
connection = sqlite3.connect('customer.db')

# creat a cursor
c = connection.cursor()

# query the database
c.execute("SELECT * FROM customers")

#fetchone()
#fetchmany(3)
print("NAME " + " \t\t" + "EMAIL")
print("______"+"\t\t"+"______")
items = c.fetchall()
for item in items:
    print(item[0] + " " + item[1] + "\t\t" + item[2])

print("command executed succesfully")

# commiting our database
connection.commit()

# close connection
connection.close()

