class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    @staticmethod
    def get_object(object_id, class_iter):
        return next(filter(lambda o: o.id == object_id, class_iter))

    def subscription_info(self, subscription_id):
        subscription = self.get_object(subscription_id, self.subscriptions)
        customer = self.get_object(subscription.customer_id, self.customers)
        trainer = self.get_object(subscription.trainer_id, self.trainers)
        plan = self.get_object(subscription.exercise_id, self.plans)
        equ = self.get_object(plan.equipment_id, self.equipment)

        result = [repr(subscription), repr(customer), repr(trainer), repr(equ), repr(plan)]
        return "\n".join(result)
