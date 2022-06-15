from multiprocessing import connection
import sqlite3

def sqldata():
    connection = sqlite3.connect('customer.db')

    curs = connection.cursor()

    curs.execute("select rowid, * from customers")

    items = curs.fetchall()
    for item in items:
        print(item)

    connection.commit()

    connection.close()

def add_records(first,last,email):
    connection = sqlite3.connect('customer.db')
    curs = connection.cursor()

    curs.execute("insert into customers values(?,?,?)",(first,last,email))

    connection.commit()
    connection.close()

def multi_records(list):
    connection = sqlite3.connect('customer.db')
    curs = connection.cursor()

    curs.executemany("insert into customers values(?,?,?)",(list))

    connection.commit()
    connection.close()    

def delet_records(id):
    connection = sqlite3.connect('customer.db')
    curs = connection.cursor()

    curs.execute("delete from customers where rowid = (?)",id)

    connection.commit()
    connection.close()