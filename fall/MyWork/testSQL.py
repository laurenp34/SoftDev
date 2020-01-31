import sqlite3

db = sqlite3.connect("foo.db") # connect references the database or creates if doesnt alrdy exist
c = db.cursor() # returns cursor object. (a set of rows + pointer for current row)

c.execute("DROP TABLE roster")
c.execute("CREATE TABLE IF NOT EXISTS roster (name TEXT, userid INTEGER)")

stmt1 = "INSERT INTO roster VALUES ('Quentin', 20)"
stmt2 = "INSERT INTO roster VALUES ('Lauren', 17)"

c.execute(stmt1)
c.execute(stmt2)

db.commit()

c.execute('SELECT * FROM roster')
print(c.fetchall())

db.close()
