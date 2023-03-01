import sqlite3
from pprint import pprint

from shop.models import Product, Category


con = sqlite3.connect("database.db")
cur = con.cursor()

# macbook = Product("Macbook AIR", 'Apple', 'Macbook', 1000)
# macbook.save_to_db(cur)

cur.execute("""UPDATE product SET (category_id)=(Null)""")
con.commit()

cur.execute("""SELECT * FROM product""")
pprint(cur.fetchall())