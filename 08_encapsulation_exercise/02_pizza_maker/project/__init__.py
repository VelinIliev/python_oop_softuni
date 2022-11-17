# from dough import Dough
# from pizza import Pizza
# from topping import Topping
#
# t = Topping("Tomato", 20)
# self.assertEqual(t.topping_type, "Tomato")
# self.assertEqual(t.weight, 20)
#
# t = Topping("", 20)
# self.assertEqual("The topping type cannot be an empty string", str(ve.exception))
#
# t = Topping("a", -1)
# self.assertEqual("The weight cannot be less or equal to zero", str(ve.exception))
#
# d = Dough("Sugar", "Mixing", 20)
# print(d.flour_type)  # , "Sugar")
# print(d.baking_technique) #, "Mixing")
# print(d.weight) #, 20)
#
#
# d = Dough("", 'ab', 20)
# pr("The flour type cannot be an empty string", str(ve.exception))
#
#
# d = Dough("ab", '', 20)
#     self.assertEqual("The baking technique cannot be an empty string", str(ve.exception))
#
#
# t = Dough("a", 'ab', -1)
#     self.assertEqual("The weight cannot be less or equal to zero", str(ve.exception))
#
#
# d = Dough("Sugar", "Mixing", 20)
# p = Pizza("Burger", d, 5)
#
# print(p.name) #, "Burger")
# print(p.dough) #, d)
# print(len(p.toppings)) #, 0)
# print(p.toppings_capacity) #, 5)
#
#
# d = Dough("Sugar", "Mixing", 20)
# t = Topping("Tomato", 20)
# p = Pizza("Burger", d, 1)
# p.add_topping(t)
# p.add_topping(t)
# self.assertEqual("Not enough space for another topping", str(ctx.exception))
#
#
# d = Dough("Sugar", "Mixing", 20)
# t = Topping("Tomato", 20)
# p = Pizza("Burger", d, 200)
# p.add_topping(t)
# #
# print(p.toppings["Tomato"]) #, 20)
# print(len(p.toppings)) #, 1)
#
#
# d = Dough("Sugar", "Mixing", 20)
# t = Topping("Tomato", 20)
# p = Pizza("Burger", d, 200)
# p.add_topping(t)
# p.add_topping(t)
#
# print(p.toppings["Tomato"]) #, 40)
#
#
# d = Dough("Sugar", "Mixing", 20)
# t = Topping("Tomato", 20)
# p = Pizza("Burger", d, 200)
# p.add_topping(t)
# p.add_topping(t)
#
# print(p.calculate_total_weight()) #, 60)
