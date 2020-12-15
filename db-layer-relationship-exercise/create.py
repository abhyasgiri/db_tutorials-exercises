from app import db, Customers, Products, Orders
db.drop_all()
db.create_all() # Creates all table classes defined

customer_one = Customers(name = "Abhyas", email = 'abhyasgiri@outlook.com')
customer_two = Customers(name = "Frank", email = "frank.jones@gmail.com")

product_one = Products(name = "Laptop", price = 499.99)
product_two = Products(name = "Rickenbacker 4003", price = 2300.0)

order_one = Orders(customer = customer_one, product = product_one)
order_one = Orders(customer = customer_one, product = product_two)
order_three = Orders(customer = customer_two, product = product_one)

db.session.add(customer_one)
db.session.add(customer_two)
db.session.add(product_one)
db.session.add(product_two)
db.session.add(order_one)
db.session.add(order_two)
db.session.add(order_three)
db.session.commit()