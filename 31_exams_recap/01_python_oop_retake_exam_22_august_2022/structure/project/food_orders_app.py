from project.client import Client


class FoodOrdersApp:
    receipt_id = iter([x for x in range(1, 200)])

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):

        client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list), None)

        if client:
            raise Exception('The client has already been registered!')

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)

        return f'Client {new_client.phone_number} registered successfully.'

    def add_meals_to_menu(self, *meals):

        for meal in meals:
            if meal.__class__.__name__ in ['Starter', 'MainDish', 'Dessert']:
                self.menu.append(meal)

    def show_menu(self):

        if len(self.menu) < 5:
            raise Exception('The menu is not ready!')

        return "\n".join(meal.details() for meal in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):

        client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list), None)

        if len(self.menu) < 5:
            raise Exception('The menu is not ready!')

        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        temp_order = []

        for meal_name, quantity in meal_names_and_quantities.items():

            meal = next(filter(lambda x: x.name == meal_name, self.menu), None)

            if not meal:
                raise Exception(f'{meal_name} is not on the menu!')

            if meal.quantity < quantity:
                raise Exception(f'Not enough quantity of {meal.__class__.__name__}: {meal.name}!')

            temp_order.append([meal, quantity])

        for meal, quantity in temp_order:
            amount = meal.price * quantity
            client.bill += amount
            meal.quantity -= quantity
            client.shopping_cart.append(meal)

        client.temp_order += temp_order

        return f'Client {client.phone_number} successfully ordered ' \
               f'{", ".join(x.name for x in client.shopping_cart)} for {client.bill:.2f}lv.'

    def cancel_order(self, client_phone_number: str):

        client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list), None)

        if not client.shopping_cart:
            raise Exception('There are no ordered meals!')

        for meal, quantity in client.temp_order:
            meal.quantity += quantity

        client.shopping_cart = []
        client.temp_order = []
        client.bill = 0

        return f'Client {client.phone_number} successfully canceled his order.'

    def finish_order(self, client_phone_number: str):

        client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list), None)

        if not client.shopping_cart:
            raise Exception('There are no ordered meals!')

        output = f'Receipt #{next(FoodOrdersApp.receipt_id)} with total amount of ' \
                 f'{client.bill:.2f} was successfully paid for {client.phone_number}.'

        client.shopping_cart = []
        client.bill = 0
        client.temp_bill = []

        return output

    def __str__(self):
        return f'Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients.'
