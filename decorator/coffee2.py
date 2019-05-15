from __future__ import annotations
from abc import ABC, abstractmethod


class Beverage(ABC):

    _desc = ''
    _cost = 0.0

    def get_desc(self):
        return self._desc

    def cost(self):
        return self._cost



class AddOnDecorator(Beverage, ABC):
    """ Class IS-A Beverage and HAS a Beverage"""

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_desc(self):
        return '{} {}'.format(self.beverage.get_desc(), self._desc)

    def cost(self):
        return self.beverage.cost() + self._cost


class Decaf(Beverage):
    _desc = 'Decaf'
    _cost = 1.2


class Espresso(Beverage):
    _desc = 'Espresso'
    _cost = 1.05


class LargeMilkAddOn(AddOnDecorator):
    _desc = 'Large Milk'
    _cost = 1.1


class SmallMilkAddOn(AddOnDecorator):
    _desc = 'Small Milk'
    _cost = 1.1


class CaramelAddOn(AddOnDecorator):
    _desc = 'Caramel'
    _cost = 0.25


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
