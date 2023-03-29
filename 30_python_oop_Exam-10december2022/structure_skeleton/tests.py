from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.christmas_pastry_shop_app import ChristmasPastryShopApp
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen

# g = Gingerbread("x", 2)
# print(g.name)
# print(g.portion)
# print(g.price)
# print(g.details())
# s = Stolen("x", 2)
# print(s.name)
# print(s.portion)
# print(s.price)
# print(s.details())

shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
print(shop.delicacies[0].details())
print(shop.add_booth("Open Booth", 1, 30))
print(shop.add_booth("Private Booth", 10, 5))
print(shop.reserve_booth(30))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.reserve_booth(5))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.get_income())

# booth = OpenBooth(1, 0)
# print(booth.booth_number)
# print(booth.capacity)
#
# booth2 = PrivateBooth(1, 10)
# print(booth2.booth_number)
# print(booth2.capacity)