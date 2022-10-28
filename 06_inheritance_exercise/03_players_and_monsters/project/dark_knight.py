from project.knight import Knight


class DarkKnight(Knight):
    def __str__(self):
        return f'{username} of type {__class__.__name__} has level {level}'