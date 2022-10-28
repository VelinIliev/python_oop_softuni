from project.hero import Hero


class Elf(Hero):
    def __str__(self):
        return f'{username} of type {__class__.__name__} has level {level}'