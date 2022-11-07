class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError('Invalid username!')
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError('Users under the age of 6 are not allowed!')
        self.__age = value

    def __str__(self):
        display_string = ""
        display_string += f'Username: {self.username}, Age: {self.age}\n'
        display_string += f'Liked movies:\n'
        if self.movies_liked:
            display_string += "\n".join(x.details() for x in self.movies_liked)
        else:
            display_string += 'No movies liked.'
        display_string += f'\nOwned movies:\n'
        if self.movies_owned:
            display_string += "\n".join(x.details() for x in self.movies_owned)
        else:
            display_string += 'No movies owned.'
        return display_string

