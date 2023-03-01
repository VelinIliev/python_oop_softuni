from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        product = next(filter(lambda x: x.name == product_name, self.products), None)
        return product

    def remove(self, product_name: str):
        product = next(filter(lambda x: x.name == product_name, self.products), None)
        if product:
            self.products.remove(product)

    def __repr__(self):
        output = []
        [output.append(f'{product.name}: {product.quantity}') for product in self.products]
        return '\n'.join(output)
