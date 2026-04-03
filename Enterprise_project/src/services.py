products = []
users = []
orders = []

# PRODUCT
def add_product(name, price):
    product = {"id": len(products)+1, "name": name, "price": price}
    products.append(product)
    return product

def get_products():
    return products


# USER
def add_user(username):
    user = {"id": len(users)+1, "username": username}
    users.append(user)
    return user


# ORDER
def create_order(product_id, user_id):
    order = {"id": len(orders)+1, "product_id": product_id, "user_id": user_id}
    orders.append(order)
    return order