from project.bakery import Bakery

bakery = Bakery("Bakery")
print(bakery.name)
bakery.add_food("Bread", "франзела", 2)
bakery.add_food("Bread", "хлебче", 1)
bakery.add_food("Cake", "кекс", 2.5)
print(bakery.food_menu)
bakery.add_drink("Water", "вода", 200, "Девин")
bakery.add_drink("Tea", "чай", 300, "БИОПРОГРАМ")
print(bakery.drinks_menu)
bakery.add_table("InsideTable", 1, 4)
bakery.add_table("InsideTable", 2, 12)
bakery.add_table("InsideTable", 3, 10)
bakery.add_table("OutsideTable", 51, 4)
bakery.add_table("OutsideTable", 52, 4)
bakery.add_table("OutsideTable", 53, 4)
print(bakery.tables_repository)
print(bakery.reserve_table(10))
print(bakery.reserve_table(10))
print(bakery.reserve_table(12))
print(bakery.reserve_table(1))
print(bakery.reserve_table(0))

print(bakery.order_food(2, "франзела", "хлебче", "musaka"))
print(bakery.order_drink(2, "чай", "вода", "уиски"))
print(bakery.leave_table(2))
print(bakery.get_free_tables_info())
