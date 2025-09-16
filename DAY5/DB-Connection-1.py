import sqlite3
conn = sqlite3.connect('products.db')
if(conn):
    print('DB Connection is done')

conn.execute('create table product (pid INTEGER,pname TEXT,pcost INT)')
print('DB- product table is created')

conn.close()