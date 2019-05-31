class HueLight:

    def __init__(self, name):
        self.name = name
        self.level = 100
        self.is_on = False

    def __repr__(self):
        if self.is_on and self.level:
            return f'<Hue {self.name} is on at level {self.level}%>'
        else:
            return f'<Hue {self.name} is off'

    def on(self):
        self.is_on = True
        if self.level == 0:
            self.level = 100
        print(self)

    def off(self):
        self.is_on = False
        print(self)

    def dimDown(self):
        self.is_on = True
        self.level -= 10
        if self.level < 0:
            self.level = 0
        print(self)

    def dimUp(self):
        self.is_on = True
        self.level += 10
        if self.level > 100:
            self.level = 100
        print(self)
