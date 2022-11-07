class Player:
    players = []

    def __init__(self, name, age, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self._need_sustenance = self.check_stamina()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError('Name not valid!')
        elif value in self.players:
            raise Exception(f'Name {value} is already used!')
        else:
            self.players.append(value)
            self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError('The player cannot be under 12 years old!')
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value > 100 or value < 0:
            raise ValueError('Stamina not valid!')
        self.__stamina = value

    def check_stamina(self):
        if self.stamina < 100:
            return True
        else:
            return False

    def __str__(self):
        return f'Player: {self.name}, {self.age}, {self.stamina}, {self.check_stamina()}'

    @property
    def need_sustenance(self):
        return self._need_sustenance


