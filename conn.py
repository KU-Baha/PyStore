import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

for i in range(4, 14):
    cur.execute(f"""INSERT INTO product VALUES (Null, '{sel}', 'Samsung', 'Televizor', {i*i*i}, Null)""")

con.commit()