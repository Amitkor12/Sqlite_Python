import sqlite3

# create A database
connection = sqlite3.connect('customer.db')

# creat a cursor
c = connection.cursor()

# query the database -- ordered by
# assending order
c.execute("SELECT rowid, * FROM customers ORDER BY last_name ")

# desending order
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")


#fetchone()
#fetchmany(3)
# print("NAME " + " \t\t" + "EMAIL")
# print("______"+"\t\t______")
items = c.fetchall()
for item in items:
    print(item)

print("command executed succesfully")

# commiting our database
connection.commit()

# close connection
connection.close()