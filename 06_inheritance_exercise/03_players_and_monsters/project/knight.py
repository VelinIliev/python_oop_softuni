from project.hero import Hero


class Knight(Hero):
    def __str__(self):
        return f'{self.username} of type {__class__.__name__} has level {self.level}'