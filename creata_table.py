import sqlite3

connection=sqlite3.connect('data.db')
con_cur=connection.cursor()

Table_statment="CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username varchar(255),password varchar(255))"

con_cur.execute(Table_statment)

connection.close()

