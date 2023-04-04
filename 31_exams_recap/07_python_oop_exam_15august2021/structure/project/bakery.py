from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable

food_mapper = {
    "Bread": Bread,
    "Cake": Cake
}

drink_mapper = {
    "Tea": Tea,
    "Water": Water
}

table_mapper = {
    "InsideTable": InsideTable,
    "OutsideTable": OutsideTable
}


class Bakery:
    def __init__(self, name: str):
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
        if value.strip() == '':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):

        if food_type in food_mapper:

            food = next(filter(lambda x: x.name == name, self.food_menu), None)

            if food:
                raise Exception(f"{food_type} {name} is already in the menu!")

            new_food = food_mapper[food_type](name, price)
            self.food_menu.append(new_food)

            return f'Added {new_food.name} ({food_type}) to the food menu'

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):

        if drink_type in drink_mapper:

            drink = next(filter(lambda x: x.name == name, self.drinks_menu), None)

            if drink:
                raise Exception(f"{drink_type} {name} is already in the menu!")

            new_drink = drink_mapper[drink_type](name, portion, brand)
            self.drinks_menu.append(new_drink)

            return f'Added {new_drink.name} ({new_drink.brand}) to the drink menu'

    def add_table(self, table_type: str, table_number: int, capacity: int):

        if table_type in table_mapper:

            table = next(filter(lambda x: x.table_number == table_number, self.tables_repository), None)

            if table:
                raise Exception(f'Table {table_number} is already in the bakery!')

            new_table = table_mapper[table_type](table_number, capacity)
            self.tables_repository.append(new_table)

        return f'Added table number {table_number} in the bakery'

    def reserve_table(self, number_of_people: int):

        table = next(
            filter(lambda x: x.capacity >= number_of_people and x.is_reserved == False, self.tables_repository), None)

        if not table:
            return f'No available table for {number_of_people} people'

        table.reserve(number_of_people)

        return f'Table {table.table_number} has been reserved for {number_of_people} people'

    def order_food(self, table_number: int, *food_names):

        table = next(filter(lambda x: x.table_number == table_number, self.tables_repository), None)

        if not table:
            return f'Could not find table {table_number}'

        in_menu = []
        not_in_menu = []

        for food_name in food_names:
            food = next(filter(lambda x: x.name == food_name, self.food_menu), None)

            if food:
                in_menu.append(str(food))
                table.order_food(food)
            else:
                not_in_menu.append(food_name)

        output = [f'Table {table_number} ordered:', *in_menu, f"{self.name} does not have in the menu:", *not_in_menu]

        return "\n".join(output)

    def order_drink(self, table_number: int, *drink_names):

        table = next(filter(lambda x: x.table_number == table_number, self.tables_repository), None)

        if not table:
            return f'Could not find table {table_number}'

        in_menu = []
        not_in_menu = []

        for drink_name in drink_names:
            drink = next(filter(lambda x: x.name == drink_name, self.drinks_menu), None)

            if drink:
                in_menu.append(str(drink))
                table.order_drink(drink)
            else:
                not_in_menu.append(drink_name)

        output = [f'Table {table_number} ordered:', *in_menu, f"{self.name} does not have in the menu:", *not_in_menu]

        return "\n".join(output)

    def leave_table(self, table_number: int):

        table = next(filter(lambda x: x.table_number == table_number, self.tables_repository), None)

        bill = table.get_bill()
        self.total_income += bill
        table.clear()

        return f'Table: {table_number}\n' \
               f'Bill: {bill:.2f}'

    def get_free_tables_info(self):
        return "\n".join(table.free_table_info() for table in self.tables_repository)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
