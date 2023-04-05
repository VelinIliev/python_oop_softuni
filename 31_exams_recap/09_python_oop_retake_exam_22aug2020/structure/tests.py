from project.people.child import Child
from project.rooms.alone_young import AloneYoung
from project.rooms.old_couple import OldCouple
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren

from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren
from project.people.child import Child
from project.everland import Everland

everland = Everland()


young_couple = YoungCouple("Johnsons", 150, 205)
# 
child1 = Child(5, 1, 2, 1)
child2 = Child(3, 2)
young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
# 
everland.add_room(young_couple)
everland.add_room(young_couple_with_children)
print(everland.get_monthly_consumptions())
# print(young_couple_with_children.expenses)
# print(young_couple.expenses)
print(everland.pay())
print(everland.status())


# ya = AloneYoung("Johnsons", 150, 205)
# print(ya.expenses)
# oc = OldCouple("Johnsons", 150, 205)
# print(oc.budget)
# print(oc.expenses)
# yc = YoungCouple("Johnsons", 150, 205)
# print(yc.budget)
# print(yc.expenses)
# child1 = Child(5, 1, 2, 1)
# child2 = Child(3, 2)
# ycwc = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
# print(ycwc.members_count)
# print(ycwc.appliances)
# print(ycwc.expenses)
