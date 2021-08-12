
class OnlyOne:

    instance = None

    class __OnlyOne:
        def __init__(self):
            self.val = 42

    def __new__(cls):
        if OnlyOne.instance is None:
            OnlyOne.instance = OnlyOne.__OnlyOne()
        return OnlyOne.instance


a = OnlyOne()
b = OnlyOne()
assert a is b

a.val = 43
assert b.val == 43
