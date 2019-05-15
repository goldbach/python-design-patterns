from __future__ import annotations
from abc import ABC, abstractmethod

class Observable(ABC):

    def __init__(self):
        self._observers = []

    def subscribe(self, o: Observer):
        self._observers.append(o)

    def unsubscribe(self, o: Observer):
        self._observers.remove(o)
    
    def notify_observers(self):
        for observer in self._observers:
            observer.update()


class Observer(ABC):

    def __init__(self, observable: Observable):
        self.observable = observable
        self.observable.subscribe(self)

    @abstractmethod
    def update(self):
        pass


class BusinessLogic(Observable):

    def __init__(self):
        super().__init__()
        self.result = 42

    def do_thing(self):
        # ... business logic ...
        self.result += 1
        self.notify_observers()

    def get_result(self):
        return self.result


class IwantToKnow(Observer):

    ### inherit __init__

    def update(self):
        print("Im class 1 - Got an update", self.observable.get_result())
        


class IwantToKnowToo(Observer):

    def __init__(self, observable: Observable):
        super().__init__(observable)
        # ... do your stuff here

    def update(self):
        print("Im class 2 - Got an update", self.observable.get_result())


businesslogic = BusinessLogic()
c1 = IwantToKnow(businesslogic)
c2 = IwantToKnowToo(businesslogic)

businesslogic.do_thing()

businesslogic.unsubscribe(c2)
businesslogic.do_thing()

