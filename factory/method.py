import random
from abc import ABC, abstractclassmethod


class Animal(ABC):
    pass


class Bear(Animal):
    pass


class Deer(Animal):
    pass


class Duck(Animal):
    pass


class AnimalFactory(ABC):

    @abstractclassmethod
    def createAnimal(self):
        pass

    def report(self):
        return self._animals


class RandomAnimalFactory(AnimalFactory):

    _animals = {k: 0 for k in Animal.__subclasses__()}
    @classmethod
    def createAnimal(cls):
        animal = random.choice(list(cls._animals))
        cls._animals[animal] += 1
        return()


class BalancedAnimalFactory(AnimalFactory):

    _animals = {k: 0 for k in Animal.__subclasses__()}
    @classmethod
    def createAnimal(cls):
        animal = min(cls._animals, key=cls._animals.get)
        cls._animals[animal] += 1
        return animal()


r = RandomAnimalFactory()
for _ in range(9999):
    r.createAnimal()
print("Random", r.report())


b = BalancedAnimalFactory()
for _ in range(9999):
    b.createAnimal()
print("Balanced", b.report())
