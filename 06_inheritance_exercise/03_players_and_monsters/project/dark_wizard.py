from project.wizard import Wizard


class DarkWizard(Wizard):
    def __str__(self):
        return f'{username} of type {__class__.__name__} has level {level}'
