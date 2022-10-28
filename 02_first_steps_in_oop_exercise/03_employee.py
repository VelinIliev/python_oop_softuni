class Employee:
    def __init__(self, id: int, first_name: str, last_name: str, salary: int):
        id = id
        first_name = first_name
        last_name = last_name
        salary = salary

    def get_full_name(self):
        return f'{first_name} {last_name}'

    def get_annual_salary(self):
        return salary * 12

    def raise_salary(self, amount: int):
        salary += amount
        return salary

employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())
