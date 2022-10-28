class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        name = name
        __sprint = sprint
        __dribble = dribble
        __passing = passing
        __shooting = shooting

    def __str__(self):
        return_string = ""
        return_string += f'Player: {name}\n'
        return_string += f'Sprint: {__sprint}\n'
        return_string += f'Dribble: {__dribble}\n'
        return_string += f'Passing: {__passing}\n'
        return_string += f'Shooting: {__shooting}'
        return return_string