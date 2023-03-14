from project.animals.animal import Animal, Bird


class Owl(Bird):

    @staticmethod
    def make_sound():
        return f'Hoot Hoot'

    def feed(self, food):
        food_name = food.__class__.__name__
        if food_name == "Meat":
            self.weight += (.25 * food.quantity)
            self.food_eaten += food.quantity
        return f'{self.__class__.__name__} does not eat {food_name}!'


class Hen(Bird):

    @staticmethod
    def make_sound():
        return f'Cluck'

    def feed(self, food):
        self.weight += (.35 * food.quantity)
        self.food_eaten += food.quantity


