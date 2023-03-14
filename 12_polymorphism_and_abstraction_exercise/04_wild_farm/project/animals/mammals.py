from project.animals.animal import Mammal


class Mouse(Mammal):

    @staticmethod
    def make_sound():
        return f'Squeak'

    def feed(self, food):
        food_name = food.__class__.__name__
        if food_name in ["Vegetable", "Fruit"]:
            self.weight += (.1 * food.quantity)
            self.food_eaten += food.quantity
        return f'{self.__class__.__name__} does not eat {food_name}!'


class Cat(Mammal):

    @staticmethod
    def make_sound():
        return f'Meow'

    def feed(self, food):
        food_name = food.__class__.__name__
        if food_name in ["Meat", "Vegetable"]:
            self.weight += (.3 * food.quantity)
            self.food_eaten += food.quantity
        return f'{self.__class__.__name__} does not eat {food_name}!'


class Dog(Mammal):

    @staticmethod
    def make_sound():
        return f'Woof!'

    def feed(self, food):
        food_name = food.__class__.__name__
        if food_name == "Meat":
            self.weight += (.4 * food.quantity)
            self.food_eaten += food.quantity
        return f'{self.__class__.__name__} does not eat {food_name}!'


class Tiger(Mammal):

    @staticmethod
    def make_sound():
        return f'ROAR!!!'

    def feed(self, food):
        food_name = food.__class__.__name__
        if food_name == "Meat":
            self.weight += (1 * food.quantity)
            self.food_eaten += food.quantity
        return f'{self.__class__.__name__} does not eat {food_name}!'

