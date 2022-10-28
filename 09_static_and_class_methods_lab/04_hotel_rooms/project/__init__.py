# from hotel import Hotel
# from room import Room
#
# hotel = Hotel.from_stars(5)
#
# first_room = Room(1, 3)
# second_room = Room(2, 2)
# third_room = Room(3, 1)
#
# hotel.add_room(first_room)
# hotel.add_room(second_room)
# hotel.add_room(third_room)
#
# hotel.take_room(1, 4)
# hotel.take_room(1, 2)
# hotel.take_room(3, 1)
# hotel.take_room(3, 1)
#
# print(hotel.status())
#
#
#
# room = Room(1, 3)
# hotel = Hotel("Some Hotel")
#
# print(room.number) #, 1)
# print(room.capacity) #, 3)
# print(room.guests) #, 0)
# print(room.is_taken) #, False)
#
# room.take_room(2)
# print(room.is_taken) #, True)
# print(room.guests) #, 2)
#
# result = room.take_room(4)
# print(room.is_taken) #, False)
# print(room.guests) #, 0)
# print(result) #, "Room number 1 cannot be taken")
#
# room.take_room(1)
# result = room.take_room(1)
# print(room.is_taken) #, True)
# print(room.guests) #, 1)
# print(result) #, "Room number 1 cannot be taken")
#
# room.take_room(1)
# room.free_room()
# print(room.is_taken) #, False)
# print(room.guests) #, 0)
#
# result = room.free_room()
# print(room.is_taken) #, False)
# print(room.guests) #, 0)
# print(result) #, "Room number 1 is not taken")
#
# print(hotel.name) #, "Some Hotel")
# print(hotel.rooms) #, [])
# print(hotel.guests) #, 0)
#
# hotel = Hotel.from_stars(3)
# print(hotel.name) #, "3 stars Hotel")
# print(hotel.rooms) #, [])
# print(hotel.guests) #, 0)
#
# room = Room(1, 3)
# hotel.add_room(room)
# print(hotel.rooms) #, [room])
# #
# room = Room(1, 3)
# hotel.add_room(room)
# hotel.take_room(1, 3)
# print(hotel.rooms[0].is_taken) #, True)
#
# room = Room(1, 3)
# hotel.add_room(room)
# hotel.take_room(1, 3)
# hotel.free_room(1)
# print(hotel.guests) #, 0)
# print(hotel.rooms[0].is_taken) #, False)
# print(hotel.rooms[0].guests) #, 0)
#
# room = Room(1, 3)
# hotel.add_room(room)
# hotel.take_room(1, 3)
# res = hotel.status().strip()
# actual = 'Hotel Some Hotel has 3 total guests\nFree rooms: \nTaken rooms: 1'
# print(res)
