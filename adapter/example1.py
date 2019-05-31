from abc import ABC, abstractmethod


class Target(ABC):

    @abstractmethod
    def request(self, a, b):
        pass


class MajorVersion1(Target):

    def request(self, a, b):
        return a-b


class MajorVersion2(Target):

    def request(self, b, a):
        return a-b


class Client:

    def do_something(self, target):
        return target.request(2, 5)


class Adapter(Target):

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self, a, b):
        return self.adaptee.request(b, a)


v1 = MajorVersion1()
v2 = Adapter(MajorVersion2())
c = Client()
assert c.do_something(v1) == c.do_something(v2)
print("ok")
