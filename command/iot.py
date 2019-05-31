from abc import ABC, abstractmethod
from danfoss.heater import Heater
from philips.hue import HueLight


class Command(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def unexecute(self):  # undo
        pass


class HueLightOnCommand:

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def unexecute(self):
        self.light.off()


class HueLightOffCommand:

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def unexecute(self):
        self.light.on()


class HueLightDimDownCommand:

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.dimDown()

    def unexecute(self):
        self.light.dimUp()


class HueLightDimUpCommand:

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.dimUp()

    def unexecute(self):
        self.light.dimDown()


class HeaterTurnOnCommand:

    def __init__(self, heater):
        self.heater = heater

    def execute(self):
        self.heater.turn_on()

    def unexecute(self):
        self.heater.turn_off()


class HeaterTurnOffCommand:

    def __init__(self, heater):
        self.heater = heater

    def execute(self):
        self.heater.turn_off()

    def unexecute(self):
        self.heater.turn_on()


class HeaterTurnDownCommand:

    def __init__(self, heater):
        self.heater = heater

    def execute(self):
        self.heater.setTemperature(self.heater.getTemperature() - 1)

    def unexecute(self):
        self.heater.setTemperature(self.heater.getTemperature() + 1)


class HeaterTurnUpCommand:

    def __init__(self, heater):
        self.heater = heater

    def execute(self):
        self.heater.setTemperature(self.heater.getTemperature() + 1)

    def unexecute(self):
        self.heater.setTemperature(self.heater.getTemperature() - 1)


class The4ButtonInvoker:

    def __init__(self,
                 onButton: Command,
                 offButton: Command,
                 upButton: Command,
                 downButton: Command):

        self.onButton = onButton
        self.offButton = offButton
        self.upButton = upButton
        self.downButton = downButton

    def pressOn(self):
        self.onButton.execute()

    def pressOff(self):
        self.offButton.execute()

    def pressUp(self):
        self.upButton.execute()

    def pressDown(self):
        self.downButton.execute()


class IotToggleInvoker:

    def __init__(self, *commands):
        self.commands = commands
        self.toggle = True

    def press(self):
        if self.toggle:
            for cmd in self.commands:
                cmd.execute()
        else:
            for cmd in self.commands:
                cmd.unexecute()
        self.toggle = not self.toggle


kitchen_light = HueLight('Kitchen')
livingroom_light = HueLight('Living Room')
livingroom_heater = Heater('Living Room')


button = IotToggleInvoker(HueLightOnCommand(kitchen_light))
button.press()
button.press()
button.press()

livingroom_light_ctrl = The4ButtonInvoker(
    onButton=HueLightOnCommand(livingroom_light),
    offButton=HueLightOffCommand(livingroom_light),
    downButton=HueLightDimDownCommand(livingroom_light),
    upButton=HueLightDimUpCommand(livingroom_light)
)
livingroom_light_ctrl.pressDown()
livingroom_light_ctrl.pressDown()
livingroom_light_ctrl.pressDown()


livingroom_heater_ctrl = The4ButtonInvoker(
    onButton=HeaterTurnOnCommand(livingroom_heater),
    offButton=HeaterTurnOffCommand(livingroom_heater),
    upButton=HeaterTurnUpCommand(livingroom_heater),
    downButton=HeaterTurnDownCommand(livingroom_heater)
)
livingroom_heater_ctrl.pressOn()
livingroom_heater_ctrl.pressUp()
livingroom_heater_ctrl.pressUp()
livingroom_heater_ctrl.pressUp()


leave_house_button = IotToggleInvoker(
    HueLightOffCommand(kitchen_light),
    HueLightOffCommand(livingroom_light),
    HeaterTurnOffCommand(livingroom_heater)
)
leave_house_button.press()
leave_house_button.press()
