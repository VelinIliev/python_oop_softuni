class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        return f'{self.name} {other.surname}'


class Group:
    def __init__(self, name, members):
        self.name = name
        self.people = members

    def __repr__(self):
        return f'Group {self.name} with members {", ".join(str(x) for x in self.people)}'

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        members = []
        for member in self.people:
            members.append(member)
        for member in other.people:
            members.append(member)
        group_name = f'{self.name} {other.name}'
        return Group(group_name, members)

    def __getitem__(self, item):
        return f'Person {item}: {self.people[item]}'


# p0 = Person('Aliko', 'Dangote')
# p1 = Person('Bill', 'Gates')
# p2 = Person('Warren', 'Buffet')
# p3 = Person('Elon', 'Musk')
# p4 = p2 + p3
#
# first_group = Group('__VIP__', [p0, p1, p2])
# second_group = Group('Special', [p3, p4])
# third_group = first_group + second_group
# #
# print(len(first_group))
# print(second_group)
# print(third_group[0])
# #
# for person in third_group:
#     print(person)


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')


print(p0.name, 'Aliko')
print(p0.surname, 'Dangote')

print(str(p1), 'Bill Gates')

print(str(p2 + p3), 'Warren Musk')


first_group = Group('__VIP__', [p0, p1, p2])
print(first_group.name, '__VIP__')
print(first_group.people, [p0, p1, p2])

first_group = Group('__VIP__', [p0, p1, p2])
print(str(first_group), "Group __VIP__ with members Aliko Dangote, Bill Gates, Warren Buffet")

first_group = Group('__VIP__', [p0, p1, p2])
print(len(first_group), 3)
