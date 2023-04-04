from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.controller import Controller

c = Controller()
print(c.add_aquarium("FreshwaterAquarium", "Test1"))
print(c.add_aquarium("SaltwaterAquarium", "Test2"))
print(c.add_aquarium("SaltwaterAquariu", "Test3"))
print(c.add_aquarium("SaltwaterAquarium", "Test4"))
# print(c.aquariums)

print(c.add_decoration("Ornament"))
print(c.add_decoration("Ornament"))
print(c.add_decoration("Ornaments"))

print(c.add_decoration("Plant"))
# print(c.decorations_repository.decorations)

print(c.insert_decoration("Test1", "Ornament"))
print(c.insert_decoration("Test2", "Plant"))
print(c.insert_decoration("Test2", "Plants"))
# print(c.decorations_repository.decorations)

print(c.add_fish("Test1", "FreshwaterFish", "Fish1", "Species1", 2.00))
print(c.add_fish("Test1", "FreshwaterFish", "Fish3", "Species1", 2.00))
print(c.add_fish("Test2", "SaltwaterFish", "Fish2", "Species1", 2.00))

print(c.add_fish("Test1", "SaltwaterFisha", "Fish2", "Species1", 2.00))

print(c.feed_fish("Test2"))
print(c.feed_fish("Test1"))

print(c.calculate_value("Test1"))
print(c.decorations_repository.decorations[0].price)
print(c.report())

# a = FreshwaterAquarium("test3")
# print(a.__str__())
# print(c.decorations_repository.decorations[0].comfort)
