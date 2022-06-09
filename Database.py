import sqlite3

# create A database
connection = sqlite3.connect('customer.db')

# creat a cursor
c = connection.cursor()

# providing table content 
c.execute(" INSERT INTO customers VALUES ('Amit','Korgoankar','amitkor@gmail.com')")

# commiting our database
connection.commit()

# close connection
connection.close()

