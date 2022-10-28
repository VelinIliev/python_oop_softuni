from project.product import Product


class ProductRepository:
    def __init__(self):
        products = []

    def add(self, product: Product):
        products.append(product)

    def find(self, product_name: str):
        for product in products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str):
        print(products)
        for i, product in enumerate(products):
            if product.name == product_name:
                products.pop(i)

    def __repr__(self):
        return_string = ""
        for n, product in enumerate(products):
            if n == len(products) - 1:
                return_string += f'{product.name}: {product.quantity}'
            else:
                return_string += f'{product.name}: {product.quantity}\n'
        return return_string
