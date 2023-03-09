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
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        current_subscription = next(filter(lambda x: x.id == subscription_id, self.subscriptions), None)
        customer_id = current_subscription.customer_id
        current_customer = next(filter(lambda x: x.id == customer_id, self.customers), None)
        trainer_id = current_subscription.trainer_id
        current_trainer = next(filter(lambda x: x.id == trainer_id, self.trainers), None)
        plan_id = current_subscription.exercise_id
        current_plan = next(filter(lambda x: x.id == plan_id, self.plans), None)
        equipment_id = current_plan.equipment_id
        current_equipment = next(filter(lambda x: x.id == equipment_id, self.equipment), None)

        output = [
            "",
            f'{current_subscription}',
            f'{current_customer}',
            f'{current_trainer}',
            f'{current_equipment}',
            f'{current_plan}'
        ]
        return "\n".join(output)
