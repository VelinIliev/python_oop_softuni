from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str):
        print(self.products)
        for i, product in enumerate(self.products):
            if product.name == product_name:
                self.products.pop(i)

    def __repr__(self):
        return_string = ""
        for n, product in enumerate(self.products):
            if n == len(self.products) - 1:
                return_string += f'{product.name}: {product.quantity}'
            else:
                return_string += f'{product.name}: {product.quantity}\n'
        return return_string
