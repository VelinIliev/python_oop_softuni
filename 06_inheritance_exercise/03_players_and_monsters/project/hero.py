class Hero:
    def __init__(self, username: str, level: int):
        username = username
        level = level

    def __str__(self):
        return f'{username} of type {__class__.__name__} has level {level}'

