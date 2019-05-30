class Borg:
    shared_state = {}

    def __init__(self):
        self.__dict__ = self.shared_state


class MySingleton(Borg):

    def __init__(self):
        super().__init__()
        self.val = 42


a = MySingleton()
b = MySingleton()
assert a != b

a.val = 43
assert b.val == 43
