from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    def __init__(self, name: str, capacity=50):
        super().__init__(name, capacity)

        self.suitable_for = 'FreshwaterFish'
