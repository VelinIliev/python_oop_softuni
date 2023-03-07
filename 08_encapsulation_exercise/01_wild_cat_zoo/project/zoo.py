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

        return f'Not enough space for animal'

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'

        return f'Not enough space for worker'

    def fire_worker(self, worker_name: str):
        worker = next(filter(lambda x: x.name == worker_name, self.workers), None)
        if worker:
            self.workers.remove(worker)
            return f'{worker_name} fired successfully'

        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        salaries = sum(worker.salary for worker in self.workers)
        if self.__budget - salaries >= 0:
            self.__budget -= salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'

        return f'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        animal_expenses = sum(animal.money_for_care for animal in self.animals)
        if self.__budget - animal_expenses >= 0:
            self.__budget -= animal_expenses
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

        return f'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        output = []
        lions = list(filter(lambda x: x.__class__.__name__ == "Lion", self.animals))
        tigers = list(filter(lambda x: x.__class__.__name__ == "Tiger", self.animals))
        cheetahs = list(filter(lambda x: x.__class__.__name__ == "Cheetah", self.animals))

        output.append(f'You have {len(self.animals)} animals')
        output.append(f'----- {len(lions)} Lions:')
        output.append("\n".join(str(lion) for lion in lions))
        output.append(f'----- {len(tigers)} Tigers:')
        output.append("\n".join(str(tiger) for tiger in tigers))
        output.append(f'----- {len(tigers)} Cheetahs:')
        output.append("\n".join(str(cheetah) for cheetah in cheetahs))

        return '\n'.join(output)

    def workers_status(self):
        output = []
        keepers = list(filter(lambda x: x.__class__.__name__ == "Keeper", self.workers))
        caretakers = list(filter(lambda x: x.__class__.__name__ == "Caretaker", self.workers))
        vets = list(filter(lambda x: x.__class__.__name__ == "Vet", self.workers))

        output.append(f'You have {len(self.workers)} workers')
        output.append(f'----- {len(keepers)} Keepers:')
        output.append(f"\n".join(str(keeper) for keeper in keepers))
        output.append(f'----- {len(keepers)} Caretakers:')
        output.append(f"\n".join(str(caretaker) for caretaker in caretakers))
        output.append(f'----- {len(keepers)} Vets:')
        output.append(f"\n".join(str(vet) for vet in vets))

        return '\n'.join(output)
