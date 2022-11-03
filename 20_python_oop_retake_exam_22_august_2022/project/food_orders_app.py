from project.client import Client


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception('The client has already been registered!')
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f'Client {client_phone_number} registered successfully.'

    def add_meals_to_menu(self, *args):
        for meal in args:
            class_name = meal.__class__.__name__
            if class_name == "Starter" or class_name == "MainDish" or class_name == "Dessert":
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception('The menu is not ready!')
        return "\n".join([x.details() for x in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number, **kwargs):
        if len(self.menu) < 5:
            raise Exception('The menu is not ready!')
        current_client = None
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                current_client = client
        if not current_client:
            current_client = Client(client_phone_number)
            self.clients_list.append(current_client)
        meals = []
        price = 0
        for meal_name, quantity in kwargs.items():
            meal_found = False
            for meal in self.menu:
                if meal.name == meal_name:
                    meal_found = True
                    meals.append([meal, quantity])
                    price += meal.price * quantity
            if not meal_found:
                raise Exception(f'{meal_name} is not on the menu!')
            for current_meal in meals:
                if current_meal[0].quantity < current_meal[1]:
                    raise Exception(f'Not enough quantity of {current_meal[0].__class__.__name__}: {current_meal[0].name}!')
        for x in meals:
            ordered_meal = x[0]
            quantity = x[1]
            ordered_meal.quantity -= quantity
            current_client.shopping_cart.append(ordered_meal)
        current_client.bill += price
        current_client.temp_shopping_cart += meals
        return f'Client {client_phone_number} successfully ordered {", ".join([x.name for x in current_client.shopping_cart])} for {current_client.bill:.2f}lv.'

    def cancel_order(self, client_phone_number):
        current_client = None
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                current_client = client
        if len(current_client.shopping_cart) == 0:
            raise Exception('There are no ordered meals!')
        for x in current_client.temp_shopping_cart:
            meal = x[0]
            quantity = x[1]
            meal.quantity += quantity

        current_client.bill = 0
        current_client.shopping_cart = []
        current_client.temp_shopping_cart = []
        return f'Client {client_phone_number} successfully canceled his order.'

    def finish_order(self, client_phone_number: str):
        current_client = None
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                current_client = client
        if len(current_client.shopping_cart) == 0:
            raise Exception('There are no ordered meals!')
        paid_money = current_client.bill
        current_client.bill = 0
        current_client.temp_shopping_cart = []
        current_client.shopping_cart = []
        self.receipt_id += 1
        return f'Receipt #{self.receipt_id} with total amount of {paid_money:.2f} was successfully paid for {client_phone_number}.'

    def __str__(self):
        return f'Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients.'

