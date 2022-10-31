from project.animals.animal import Mammal


class Mouse(Mammal):
    def make_sound(self):
        return f'Squeak'

    def feed(self, food):
        if food.__class__.__name__ == "Vegetable" or \
                food.__class__.__name__ == "Fruit":
            self.weight += (.1 * food.quantity)
            self.food_eaten += food.quantity
        else:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'


class Cat(Mammal):
    def make_sound(self):
        return f'Meow'

    def feed(self, food):
        if food.__class__.__name__ == "Meat" or \
                food.__class__.__name__ == "Vegetable":
            self.weight += (.3 * food.quantity)
            self.food_eaten += food.quantity
        else:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'


class Dog(Mammal):
    def make_sound(self):
        return f'Woof!'

    def feed(self, food):
        if food.__class__.__name__ == "Meat":
            self.weight += (.4 * food.quantity)
            self.food_eaten += food.quantity
        else:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'


class Tiger(Mammal):
    def make_sound(self):
        return f'ROAR!!!'

    def feed(self, food):
        if food.__class__.__name__ == "Meat":
            self.weight += (1 * food.quantity)
            self.food_eaten += food.quantity
        else:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

