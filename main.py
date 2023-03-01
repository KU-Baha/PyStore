from shop.models import Product, Category

phone = Category('Phones')

iphone15 = Product('Iphone 15 black', 'Apple', 'iphone 15', 990, 'black', 256, category=phone)
samsung = Product('Samsung S23', 'Samsung', 'S23', 850, 'white', 512, category=phone)

print(iphone15.__dict__)
print(samsung.__dict__)
