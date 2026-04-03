class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username


class Order:
    def __init__(self, id, product_id, user_id):
        self.id = id
        self.product_id = product_id
        self.user_id = user_id