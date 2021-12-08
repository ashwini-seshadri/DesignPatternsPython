#base class for all beverages
class Beverage:
    def __init__(self):
        self.description = "Unknown Beverage"
    
    def get_description(self):
        return self.description

    def cost(self):
        raise NotImplementedError


class CondimentDecorator(Beverage):
    def get_description(self):
        raise NotImplementedError

    def cost(self):
        raise NotImplementedError


class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"

    def cost(self):
        return 1.99

class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House blend coffee"

    def cost(self):
        return 0.89

class Decaf(Beverage):
    def __init__(self):
        self.description = "Decaf"

    def cost(self):
        return 1.05

class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark roast"

    def cost(self):
        return 0.99

class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return 0.20 + self.beverage.cost()

class Soy(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return 0.15 + self.beverage.cost()

class Whip(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Whip"

    def cost(self):
        return 0.10 + self.beverage.cost()

class SteamedMilk(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def get_description(self):
        return self.beverage.get_description() + ", Steamed milk"

    def cost(self):
        return 0.10 + self.beverage.cost()

def star_buzz_coffee():
    beverage = Espresso()
    print(f"{beverage.get_description()} ${beverage.cost()}")
    
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f"{beverage2.get_description()} ${beverage.cost()}")

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"{beverage3.get_description()} ${beverage3.cost()}")

star_buzz_coffee()
    



