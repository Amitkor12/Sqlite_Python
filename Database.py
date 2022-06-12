import sqlite3

# create A database
connection = sqlite3.connect('customer.db')

# creat a cursor
c = connection.cursor()

# query the database -- And/Or
c.execute("SELECT rowid, * FROM customers WHERE first_name like 'A%' AND last_name like 'Kor%'")

items = c.fetchall()
for item in items:
    print(item)

print("command executed succesfully")

# commiting our database
connection.commit()

# close connection
connection.close()