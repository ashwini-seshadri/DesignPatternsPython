class FlyBehavior:
    def fly(self):
        raise NotImplementedError

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with rocket!")

class QuackBehavior:
    def quack(self):
        raise NotImplementedError

class Quack(QuackBehavior):
    def quack(self):
        print("Quack")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("I'm mute!")

class Squeak(QuackBehavior):
    def quack(self):
        print("I squeak!")

class Duck:
    fly_behavior = None
    quack_behavior = None

    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior

    def display(self):
        raise NotImplementedError

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim():
        print("All ducks float, even decoys!")

class MallardDuck(Duck):
    fly_behavior = FlyWithWings()
    quack_behavior = Quack()

    def display(self):
        print("I'm a real mallard duck!")

class ModelDuck(Duck):
    fly_behavior = FlyNoWay()
    quack_behavior = Squeak()

    def display(self):
        print("I'm a model duck!")

mallard = MallardDuck()
mallard.perform_quack()
mallard.perform_fly()

model = ModelDuck()
model.perform_fly()
model.set_fly_behavior(FlyRocketPowered())
model.perform_fly()