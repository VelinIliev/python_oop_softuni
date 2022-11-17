class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget - price >= 0 and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        elif len(self.animals) < self.__animal_capacity and self.__budget - price < 0:
            return f'Not enough budget'
        else:
            return f'Not enough space for animal'

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        else:
            return f'Not enough space for worker'

    def fire_worker(self, worker_name: str):
        for i, worker in enumerate(self.workers):
            if worker.name == worker_name:
                self.workers.pop(i)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        salaries = [worker.salary for worker in self.workers]
        if self.__budget - sum(salaries) >= 0:
            self.__budget -= sum(salaries)
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        else:
            return f'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        animal_expenses = [animal.money_for_care for animal in self.animals]
        if self.__budget - sum(animal_expenses) >= 0:
            self.__budget -= sum(animal_expenses)
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        else:
            return f'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        return_string = ""
        lions = [animal for animal in self.animals if animal.__class__.__name__ == "Lion"]
        tigers = [animal for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == "Cheetah"]

        return_string += f'You have {len(self.animals)} animals\n'
        return_string += f'----- {len(lions)} Lions:\n'
        return_string += "\n".join(str(lion) for lion in lions)
        return_string += f'\n----- {len(tigers)} Tigers:\n'
        return_string += "\n".join(str(tiger) for tiger in tigers)
        return_string += f'\n----- {len(cheetahs)} Cheetahs:\n'
        return_string += "\n".join(str(cheetah) for cheetah in cheetahs)
        return return_string

    def workers_status(self):
        return_string = ""
        keepers = [worker for worker in self.workers if worker.__class__.__name__ == "Keeper"]
        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        vets = [worker for worker in self.workers if worker.__class__.__name__ == "Vet"]
        return_string += f'You have {len(self.workers)} workers\n'
        return_string += f'----- {len(keepers)} Keepers:\n'
        return_string += "\n".join(str(keeper) for keeper in keepers)
        return_string += f'\n----- {len(caretakers)} Caretakers:\n'
        return_string += "\n".join(str(caretaker) for caretaker in caretakers)
        return_string += f'\n----- {len(vets)} Vets:\n'
        return_string += "\n".join(str(vet) for vet in vets)
        return return_string