import sqlite3

connection=sqlite3.connect('item.db')
con_cur=connection.cursor()

Table_statment="CREATE TABLE IF NOT EXISTS items ( item varchar(255),prize FLOAT)"

con_cur.execute(Table_statment)

connection.close()

