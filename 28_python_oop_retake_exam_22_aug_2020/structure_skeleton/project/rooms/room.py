class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.appliances = []
        self.expenses = 0
        self.room_cost = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        total_expenses = 0
        for items in args:
            for item in items:
                total_expenses += item.get_monthly_expense()
        self.__expenses = total_expenses

    def __repr__(self):
        display_list = []
        display_list.append(f'{self.family_name} with {self.members_count} members. '
                            f'Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$')
        if self.children:
            for n, child in enumerate(self.children, 1):
                display_list.append(f'--- Child {n} monthly cost: {child.get_monthly_expense():.2f}$')
        if self.appliances:
            cost_appliances = sum(x.get_monthly_expense() for x in self.appliances)
            display_list.append(f'--- Appliances monthly cost: {cost_appliances:.2f}$')
        return "\n".join(display_list)

# room = Room(" ", 100, 3)
# room.calculate_expenses(2,-4)
# print(room.expenses)