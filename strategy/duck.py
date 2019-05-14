from abc import ABC, abstractmethod


class DuckStrategy(ABC):

    @abstractmethod
    def execute(self):
        pass


class Duck:

    def __init__(self, name: str, fly_behavior: DuckStrategy, quack_behavior: DuckStrategy):
        self.name = name
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def fly(self):
        return self.fly_behavior.execute()

    def quack(self):
        return self.quack_behavior.execute()

    def __repr__(self):
        return "I'm {} - look at me, I'm ".format(self.name) 

class DuckNormalFly(DuckStrategy):

    def execute(self):
        return 'flying normally'


class RealDuckQuack(DuckStrategy):

    def execute(self):
        return 'quack quack'


class FakeDuckQuack(DuckStrategy):

    def execute(self):
        return 'squizze'


class DuckNoFly(DuckStrategy):

    def execute(self):
        return " ... (you'll have to throw me)"


rubberduck = Duck(name='Rubber', fly_behavior=DuckNoFly(), quack_behavior=FakeDuckQuack())
greyduck = Duck(name='Grey', fly_behavior=DuckNormalFly(), quack_behavior=RealDuckQuack())


print(rubberduck, rubberduck.fly())
print(rubberduck, rubberduck.quack())
print(greyduck, greyduck.fly())
print(greyduck, greyduck.quack())
