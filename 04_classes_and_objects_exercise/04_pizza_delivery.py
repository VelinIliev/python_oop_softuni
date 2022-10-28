class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        name = name
        price = price
        ingredients = ingredients
        ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if ordered:
            return f"Pizza {name} already prepared, and we can't make any changes!"
        if ingredient in ingredients:
            ingredients[ingredient] += quantity
        else:
            ingredients[ingredient] = quantity

        price += quantity * price_per_quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if ordered:
            return f"Pizza {name} already prepared, and we can't make any changes!"
        if ingredient not in ingredients:
            return f'Wrong ingredient selected! We do not use {ingredient} in {name}!'
        elif ingredient in ingredients:
            if ingredients[ingredient] - quantity < 0:
                return f'Please check again the desired quantity of {ingredient}!'
            else:
                ingredients[ingredient] -= quantity
                price -= quantity * price_per_quantity

    def make_order(self):
        ordered = True
        return f"You've ordered pizza {name} prepared with {', '.join(f'{k}: {v}' for k,v in ingredients.items())} " \
               f"and the price will be {price}lv."

margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
