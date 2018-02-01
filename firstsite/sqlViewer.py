import sqlite3
connection = sqlite3.connect("db.sqlite3")
c = connection.cursor()
c.execute("SELECT * FROM ContactTable")