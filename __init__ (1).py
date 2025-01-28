'''
import json

import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    cart_details = dao.get_cart(username)
    if cart_details is None:
        return []
   
    items = []
    for cart_detail in cart_details:
        contents = cart_detail['contents']
        evaluated_contents = eval(contents)  
        for content in evaluated_contents:
            items.append(content)
   
    i2 = []
    for i in items:
        temp_product = products.get_product(i)
        i2.append(temp_product)
    return i2

   


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)




'''



import json
from products import Product
from cart import dao


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @classmethod
    def load(cls, data):
        contents = [Product(id=content['id'], name=content['name'], price=content['price']) for content in data['contents']]
        return cls(data['id'], data['username'], contents, data['cost'])


def get_cart(username: str) -> list:
    cart_details = dao.get_cart(username)
    if cart_details is None:
        return []

    # Assuming the 'contents' is a list of product ids in the cart
    product_ids = [content['id'] for cart_detail in cart_details for content in cart_detail['contents']]
    return [products.get_product(product_id) for product_id in product_ids]


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    dao.delete_cart(username)

