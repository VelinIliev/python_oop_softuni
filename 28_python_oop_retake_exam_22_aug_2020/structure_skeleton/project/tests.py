from project.rooms.young_couple import YoungCouple
from project.rooms.old_couple import OldCouple
from project.rooms.alone_young import AloneYoung
from project.rooms.alone_old import AloneOld
from project.rooms.young_couple_with_children import YoungCoupleWithChildren
from project.people.child import Child
from project.everland import Everland

everland = Everland()

def test_one():
    young_couple = YoungCouple("Johnsons", 150, 205)
    old_couple = OldCouple("Johnsons-old", 150, 205)
    alone_young = AloneYoung("Peterson-young", 200)
    alone_old = AloneOld("Peterson-old", 100)

    child1 = Child(5, 1, 2, 1)
    child2 = Child(3, 2)
    young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
    everland.add_room(young_couple)
    everland.add_room(old_couple)
    everland.add_room(alone_young)
    everland.add_room(alone_old)
    everland.add_room(young_couple_with_children)

    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


if __name__ == "__main__":
    test_one()