from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError('Name cannot be empty string or white space!')
        self.__name = value

    def find_food(self, name):
        food = next(filter(lambda x: x.name == name, self.food_menu), None)
        return food

    def find_drink(self, name):
        return next(filter(lambda x: x.name == name, self.drinks_menu), None)

    def find_table(self, number):
        return next(filter(lambda x: x.table_number == number, self.tables_repository), None)

    def add_food(self, food_type: str, name: str, price: float):
        if food_type == "Bread" or food_type == "Cake":
            current_food = self.find_food(name)
            if current_food:
                raise Exception(f'{food_type} {current_food.name} is already in the menu!')
            if food_type == "Bread":
                current_food = Bread(name, price)
                self.food_menu.append(current_food)
                return f'Added {name} ({food_type}) to the food menu'
            elif food_type == "Cake":
                current_food = Cake(name, price)
                self.food_menu.append(current_food)
                return f'Added {name} ({food_type}) to the food menu'

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type == "Tea" or drink_type == "Water":
            current_drink = self.find_drink(name)
            if current_drink:
                raise Exception(f'{drink_type} {name} is already in the menu!')
            if drink_type == "Tea":
                current_drink = Tea(name, portion, brand)
                self.drinks_menu.append(current_drink)
                return f'Added {name} ({brand}) to the drink menu'
            elif drink_type == "Water":
                current_drink = Water(name, portion, brand)
                self.drinks_menu.append(current_drink)
                return f'Added {name} ({brand}) to the drink menu'

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type == "InsideTable" or table_type == "OutsideTable":
            current_table = self.find_table(table_number)
            if current_table:
                raise Exception(f'Table {table_number} is already in the bakery!')
            if table_type == "InsideTable":
                current_table = InsideTable(table_number, capacity)
                self.tables_repository.append(current_table)
                return f'Added table number {table_number} in the bakery'
            elif table_type == "OutsideTable":
                current_table = OutsideTable(table_number, capacity)
                self.tables_repository.append(current_table)
                return f'Added table number {table_number} in the bakery'

    def reserve_table(self, number_of_people: int):
        free_table = next(filter(lambda x: x.is_reserved is False and x.capacity >= number_of_people,
                                 self.tables_repository), None)
        if not free_table:
            return f'No available table for {number_of_people} people'
        free_table.reserve(number_of_people)
        return f'Table {free_table.table_number} has been reserved for {number_of_people} people'

    def order_food(self, table_number: int, *food_names):
        current_table = self.find_table(table_number)
        if not current_table:
            return f'Could not find table {table_number}'
        food_in_menu = []
        food_not_in_menu = []
        for food_name in food_names:
            food = self.find_food(food_name)
            if food:
                food_in_menu.append(food.__repr__())
                current_table.food_orders.append(food)
            else:
                food_not_in_menu.append(food_name)

        display_list = [f'Table {table_number} ordered:', *food_in_menu,
                        f'{self.name} does not have in the menu:', *food_not_in_menu]
        return "\n".join(display_list)

    def order_drink(self, table_number: int, *drink_names):
        current_table = self.find_table(table_number)
        if not current_table:
            return f'Could not find table {table_number}'
        drinks_in_menu = []
        drinks_not_in_menu = []
        for drink_name in drink_names:
            drink = self.find_drink(drink_name)
            if drink:
                drinks_in_menu.append(drink.__repr__())
                current_table.drink_orders.append(drink)
            else:
                drinks_not_in_menu.append(drink_name)

        display_list = [f'Table {table_number} ordered:', *drinks_in_menu,
                        f'{self.name} does not have in the menu:', *drinks_not_in_menu]
        return "\n".join(display_list)

    def leave_table(self, table_number: int):
        current_table = self.find_table(table_number)
        table_bill = current_table.get_bill()
        display_list = [f'Table: {table_number}', f'Bill: {table_bill:.2f}']
        self.total_income += table_bill
        current_table.clear()
        return "\n".join(display_list)

    def get_free_tables_info(self):
        free_tables = []
        for table in self.tables_repository:
            if not table.is_reserved:
                free_tables.append(table.free_table_info())
        return "\n".join(free_tables)

    def get_total_income(self):
        return f'Total income: {self.total_income:.2f}lv'
