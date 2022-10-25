class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.budget = budget
        self.animal_capacity = animal_capacity
        self.workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.budget - price >= 0 and len(self.animals) < self.animal_capacity:
            self.animals.append(animal)
            self.budget -= price
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        elif len(self.animals) < self.animal_capacity and self.budget - price < 0:
            return f'Not enough budget'
        else:
            return f'Not enough space for animal'

    def hire_worker(self, worker):
        if len(self.workers) < self.workers_capacity:
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
        if self.budget - sum(salaries) >= 0:
            self.budget -= sum(salaries)
            return f'You payed your workers. They are happy. Budget left: {self.budget}'
        else:
            return f'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        animal_expenses = [animal.money_for_care for animal in self.animals]
        if self.budget - sum(animal_expenses) >= 0:
            self.budget -= sum(animal_expenses)
            return f'You tended all the animals. They are happy. Budget left: {self.budget}'
        else:
            return f'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.budget += amount

    def animals_status(self):
        return f'You have {len(self.animals)} animals'

    def workers_status(self):
        keepers = [worker for worker in self.workers if worker.__class__.__name__ == "Keeper"]
        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        vets = [worker for worker in self.workers if worker.__class__.__name__ == "Vet"]
        return f'You have {len(self.workers)} worker , {len(keepers), len(caretakers), len(vets)}'