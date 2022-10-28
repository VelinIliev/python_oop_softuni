from project.customer import Customer
from project.equipment import Equipment
from project.trainer import Trainer
from project.subscription import Subscription
from project.exercise_plan import ExercisePlan


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        added = [x for x in self.customers if x.id == customer.id]
        if not added:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        added = [x for x in self.trainers if x.id == trainer.id]
        if not added:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        added = [x for x in self.equipment if x.id == equipment.id]
        if not added:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        added = [x for x in self.plans if x.id == plan.id]
        if not added:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        added = [x for x in self.subscriptions if x.id == subscription.id]
        if not added:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        current_subscription = [x for x in self.subscriptions if x.id == subscription_id][0]
        customer_id = current_subscription.customer_id
        current_customer = [x for x in self.customers if x.id == customer_id][0]
        trainer_id = current_subscription.trainer_id
        current_trainer = [x for x in self.trainers if x.id == trainer_id][0]
        plan_id = current_subscription.exercise_id
        current_plan = [x for x in self.plans if x.id == plan_id][0]
        equipment_id = current_plan.equipment_id
        current_equipment = [x for x in self.equipment if x.id == equipment_id][0]

        return_string = ""
        return_string += f'{current_subscription}\n'
        return_string += f'{current_customer}\n'
        return_string += f'{current_trainer}\n'
        return_string += f'{current_equipment}\n'
        return_string += f'{current_plan}'
        return return_string
