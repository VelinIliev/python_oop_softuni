from project.customer import Customer
from project.dvd import DVD
from project.movie_world import MovieWorld


# c = Customer("Pesho", 22, 1)
# print(c.name) #, "Pesho")
# print(c.age) #, 22)
# print(c.id) #, 1)

c = Customer("Pesho", 22, 1)
print(repr(c)) #, "1: Pesho of age 22 has 0 rented DVD's ()")

dvd = DVD("B", 1, 2020, "January", 10)
print(dvd.name) #, "B")
print(dvd.id) #, 1)
print(dvd.creation_month) #, "January")
print(dvd.creation_year) #, 2020)
print(dvd.age_restriction) #, 10)
print(dvd.is_rented) #, False)
dvd = DVD.from_date(1, "A", "16.10.1997", 18)
print(dvd.name, "A")
print(dvd.id, 1)
print(dvd.creation_month, "October")
print(dvd.creation_year, 1997)
print(dvd.age_restriction, 18)
print(dvd.is_rented, False)

# dvd = DVD.from_date(1, "A", "16.10.1997", 18)
# print(repr(dvd)) #, "1: A (October 1997) has age restriction 18. Status: not rented")
#
# movie = MovieWorld("Test")
# print(movie.name) #, "Test")
# print(movie.customers) #, [])
# print(movie.dvds) #, [])
#
# print(MovieWorld.dvd_capacity()) #, 15)
#
# print(MovieWorld.customer_capacity(), 10)
#
# movie_world = MovieWorld("Test")
# c = Customer("Pesho", 20, 4)
# movie_world.add_customer(c)
# print(movie_world.customers, [c])
#
# movie_world = MovieWorld("Test")
# for _ in range(11):
#     movie_world.add_customer(Customer("Pesho", 20, 4))
# print(len(movie_world.customers), 10)
#
# movie_world = MovieWorld("Test")
# d = DVD("A", 1, 1254, "February", 10)
# movie_world.add_dvd(d)
# print(movie_world.dvds, [d])
#
# movie_world = MovieWorld("Test")
# for _ in range(16):
#     movie_world.add_dvd(DVD("A", 1, 1254, "February", 10))
# print(len(movie_world.dvds), 15)
#
# movie_world = MovieWorld("Test")
# d = DVD("A", 1, 1254, "February", 10)
# c = Customer("Pesho", 20, 4)
# c2 = Customer("Gosho", 26, 2)
# movie_world.add_customer(c)
# movie_world.add_customer(c2)
# movie_world.add_dvd(d)
# movie_world.rent_dvd(4, 1)
# result = movie_world.rent_dvd(2, 1)
# print(result, "DVD is already rented")
#
# movie_world = MovieWorld("Test")
# d = DVD("A", 1, 1254, "February", 10)
# c = Customer("Pesho", 20, 4)
# movie_world.add_customer(c)
# movie_world.add_dvd(d)
# movie_world.rent_dvd(4, 1)
# result = movie_world.rent_dvd(4, 1)
# print(result, "Pesho has already rented A")
#
# movie_world = MovieWorld("Test")
# d = DVD("A", 1, 1254, "February", 18)
# c = Customer("Pesho", 16, 4)
# movie_world.add_customer(c)
# movie_world.add_dvd(d)
# result = movie_world.rent_dvd(4, 1)
# print(result, "Pesho should be at least 18 to rent this movie")
#
# movie_world = MovieWorld("Test")
# d = DVD("A", 1, 1254, "February", 10)
# c = Customer("Pesho", 20, 4)
# movie_world.add_customer(c)
# movie_world.add_dvd(d)
# result = movie_world.rent_dvd(4, 1)
# print(result, "Pesho has successfully rented A")
# print(d.is_rented, True)
# print(c.rented_dvds[0], d)

# movie_world = MovieWorld("Test")
# d = DVD("A", 1, 1254, "February", 10)
# c = Customer("Pesho", 20, 4)
# movie_world.add_customer(c)
# movie_world.add_dvd(d)
# movie_world.rent_dvd(4, 1)
# result = movie_world.return_dvd(4, 1)
# print(result, "Pesho has successfully returned A")
# print(c.rented_dvds, [])
# print(d.is_rented, False)
#
# movie_world = MovieWorld("Test")
# d = DVD("A", 1, 1254, "February", 10)
# c = Customer("Pesho", 20, 4)
# movie_world.add_customer(c)
# movie_world.add_dvd(d)
# result = movie_world.return_dvd(4, 1)
# print(result, "Pesho does not have that DVD")
#
# movie_world = MovieWorld("Test")
# d = DVD("A", 1, 1254, "February", 10)
# c = Customer("Pesho", 20, 4)
# movie_world.add_customer(c)
# movie_world.add_dvd(d)
# movie_world.rent_dvd(4, 1)
# actual = repr(movie_world).strip('\n')
# expected = "4: Pesho of age 20 has 1 rented DVD's (A)\n1: A (February 1254) has age restriction 10. Status: rented"
# print(actual)

