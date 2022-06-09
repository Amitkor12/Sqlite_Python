import sqlite3

# create A database
connection = sqlite3.connect('customer.db')

# creat a cursor
c = connection.cursor()

# providing table content 
c.execute(" INSERT INTO customers VALUES ('hemant','Korgoankar','hmu@gmail.com')")
c.execute(" INSERT INTO customers VALUES ('anant','Korgoankar','anant@gmail.com')")


print("command executed succesfully")

# commiting our database
connection.commit()

# close connection
connection.close()

