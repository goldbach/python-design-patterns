class Heater:

    def __init__(self, name):
        self.name = name
        self.temperature = 20
        self.is_on = False

    def __repr__(self):
        if self.is_on:
            return f'<Heater: {self.name} is on with thermostat set to {self.temperature}'
        else:
            return f'<Heater: {self.name} is off'

    def turn_on(self):
        self.is_on = True
        print(self)

    def turn_off(self):
        self.is_on = False
        print(self)

    def getTemperature(self):
        return self.temperature

    def setTemperature(self, temp):
        self.temperature = temp
        # keep setting in (10,60) range
        self.temperature = min(self.temperature, 40)
        self.temperature = max(self.temperature, 10)
        print(self)
