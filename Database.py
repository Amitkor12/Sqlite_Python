import sqlite3

# create A database
connection = sqlite3.connect('customer.db')

# creat a cursor
c = connection.cursor()

# providing multi users at same time 
multi_customer = [('broun','wise','wise12@gmail.com'),('witley','wine','winewit@yahooh.in')]

c.executemany("INSERT INTO customers VALUES (?,?,?)", multi_customer)

print("command executed succesfully")

# commiting our database
connection.commit()

# close connection
connection.close()

