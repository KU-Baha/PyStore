class Product:
    def __init__(self, name: str, brand: str, model: str, price: int = 0, category=None):
        self.name = name
        self.brand = brand
        self.model = model
        self.price = price
        self.category = category

    def __repr__(self):
        return self.name

    def save_to_db(self, cur):
        cur.execute(f"""INSERT INTO product VALUES (Null, '{self.name}', '{self.brand}', '{self.model}', {self.price}, Null)""")


class Category:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name
