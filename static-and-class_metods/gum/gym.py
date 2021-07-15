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

    def subscription_info(self, subscription_id):
        subscription = [sub for sub in self.subscriptions if sub.id == subscription_id][0]

        customer_id = subscription.customer_id
        customer = [cus for cus in self.customers if cus.id == customer_id][0]

        trainer_id = subscription.customer_id
        trainer = [tr for tr in self.trainers if tr.id == trainer_id][0]

        plan_id = subscription.exercise_id
        plan = next(filter(lambda pl: pl.id == plan_id, self.plans))
        # plan = [pl for pl in self.plans if pl.id == plan_id][0]

        equ_id = plan.equipment_id
        equ = next(eq for eq in self.equipment if eq.id == equ_id)
        # equ = [eq for eq in self.equipment if eq.id == equ_id][0]

        result = [repr(subscription), repr(customer), repr(trainer), repr(equ), repr(plan)]

        return "\n".join(result)
