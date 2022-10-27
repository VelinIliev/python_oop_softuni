class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def __str__(self):
        return_string = ""
        return_string += f'Player: {self.name}\n'
        return_string += f'Sprint: {self.__sprint}\n'
        return_string += f'Dribble: {self.__dribble}\n'
        return_string += f'Passing: {self.__passing}\n'
        return_string += f'Shooting: {self.__shooting}'
        return return_string