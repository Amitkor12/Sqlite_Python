import sqlite3

# create A database
connection = sqlite3.connect('customer.db')

# creat a cursor
c = connection.cursor()

# query the database
# c.execute("SELECT rowid, * FROM customers")

# using where cluase
# deleting records
c.execute(""" DELETE FROM customers 
              WHERE rowid = '3'
 
""")

c.execute("SELECT * FROM customers")

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