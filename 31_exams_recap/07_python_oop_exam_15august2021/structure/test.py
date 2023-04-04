from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.bakery import Bakery
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable

# drink1 = Water("Water", 200, "Bankq")
# drink2 = Tea("Tea", 200, "HotTea")
# print(drink1)
# print(drink2)
# bakery1 = Bread("Bread", 2.00)
# bakery2 = Cake("Cake", 1.00)
# print(bakery1)
# print(bakery2)

# table1 = OutsideTable(60, 10)
# table2 = InsideTable(10, 10)
# print(table1)
# print(table2)

b = Bakery("Bakery")
print(b.add_food("Bread", "Bread", 2.00))
print(b.add_food("Cake", "Cake", 1.00))
print(b.add_drink("Water", "Water", 200, "Bankia"))
print(b.add_drink("Tea", "Tea", 200, "HotTea"))
print(b.add_table("InsideTable", 10, 10))
print(b.add_table("OutsideTable", 60, 10))
print(b.reserve_table(5))
print(b.order_food(10, "Bread", "Cake", "Some", "other"))
print(b.order_drink(10, "Water", "Tea", "Some", "other"))
print(b.leave_table(10))
print(b.get_free_tables_info())
print(b.get_total_income())

