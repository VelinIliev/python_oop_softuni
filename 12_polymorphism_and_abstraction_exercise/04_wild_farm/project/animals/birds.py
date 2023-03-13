from project.animals.animal import Animal, Bird


class Owl(Bird):
    def make_sound(self):
        return f'Hoot Hoot'

    def feed(self, food):
        if food.__class__.__name__ == "Meat":
            self.weight += (.25 * food.quantity)
            self.food_eaten += food.quantity
        else:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'


class Hen(Bird):
    def make_sound(self):
        return f'Cluck'

    def feed(self, food):
        self.weight += (.35 * food.quantity)
        self.food_eaten += food.quantity


