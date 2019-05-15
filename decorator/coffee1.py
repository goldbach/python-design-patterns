from __future__ import annotations
from abc import ABC, abstractmethod


class Beverage(ABC):

    @abstractmethod
    def get_desc(self):
        pass

    @abstractmethod
    def cost(self):
        pass



class AddOnDecorator(Beverage, ABC):
    """ Class IS-A Beverage and HAS a Beverage"""

    def __init__(self, beverage: Beverage):
        self.beverage = beverage


class Decaf(Beverage):

    def get_desc(self):
        return 'Decaf'

    def cost(self):
        return 1.2

class Espresso(Beverage):

    def get_desc(self):
        return 'Espresso'
    
    def cost(self):
        return 1.05


class LargeMilkAddOn(AddOnDecorator):

    def get_desc(self):
        return '{} {}'.format(self.beverage.get_desc(), 'Large Milk')

    def cost(self):
        return self.beverage.cost() + 1.1


class SmallMilkAddOn(AddOnDecorator):

    def get_desc(self):
        return '{} {}'.format(self.beverage.get_desc(), 'Small Milk')

    def cost(self):
        return self.beverage.cost() + 1.1


class CaramelAddOn(AddOnDecorator):

    def get_desc(self):
        return '{} {}'.format(self.beverage.get_desc(), 'Caramel')

    def cost(self):
        return self.beverage.cost() + 0.25


class Discount(AddOnDecorator):

    def __init__(self, beverage: Beverage, discount=0.9):
        super().__init__(beverage)
        self._discount = discount

    def get_desc(self):
        return '*** DISCOUNT {} ***'.format(self.beverage.get_desc())

    def cost(self):
        return self.beverage.cost() * self._discount


cup1 = CaramelAddOn(LargeMilkAddOn(Espresso()))
cup2 = Discount(SmallMilkAddOn(Espresso()), discount=0.8)

print(cup1.get_desc(), cup1.cost())
print(cup2.get_desc(), cup2.cost())
