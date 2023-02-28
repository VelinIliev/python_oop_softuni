from project.hero import Hero
from project.elf import Elf
from project.wizard import Wizard
from project.knight import Knight
from project.blade_knight import BladeKnight
from project.dark_knight import DarkKnight
from project.dark_wizard import DarkWizard
from project.muse_elf import MuseElf
from project.soul_master import SoulMaster

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)

dk = DarkKnight("DK", 2)
print(str(dk))
print(dk.__class__.__bases__[0].__name__)
bk = BladeKnight("BK", 3)
print(str(bk))
print(bk.__class__.__bases__[0].__name__)
dw = DarkWizard("DW", 4)
print(str(dw))
print(dw.__class__.__bases__[0].__name__)
k = Knight("K", 5)
print(str(k))
print(k.__class__.__bases__[0].__name__)
me = MuseElf("ME", 6)
print(str(me))
print(me.__class__.__bases__[0].__name__)
sm = SoulMaster("SM", 7)
print(str(sm))
print(sm.__class__.__bases__[0].__name__)
w = Wizard("W", 8)
print(str(w))
print(w.__class__.__bases__[0].__name__)
h = Hero("H", 9)
print(str(h))
print(h.__class__.__bases__[0].__name__)