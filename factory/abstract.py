from abc import ABC, abstractmethod


class Button(ABC):

    def __init__(self):
        self._name = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abstractmethod
    def __repr__(self):
        pass


class Alert(ABC):

    def __init__(self):
        self._txt = ''

    @property
    def txt(self):
        return self._txt

    @txt.setter
    def txt(self, txt):
        self._txt = txt

    @abstractmethod
    def __repr__(self):
        pass


class LightThemeButton(Button):

    def __repr__(self):
        return "<I'm a button in light: {}>".format(self.name)


class DarkThemeButton(Button):

    def __repr__(self):
        return "<I'm a button in dark: {}>".format(self.name)


class LightThemeAlert(Alert):

    def __repr__(self):
        return "<I'm an alert in light: {}>".format(self.txt)


class DarkThemeAlert(Alert):

    def __repr__(self):
        return "<I'm an alert in dark: {}>".format(self.txt)


class WidgetFactory(ABC):

    @abstractmethod
    def getButton():
        pass

    @abstractmethod
    def getAlert():
        pass


class LigthThemeWidgetFactory(WidgetFactory):

    def getButton(self):
        return LightThemeButton()

    def getAlert(self):
        return LightThemeAlert()


class DarkThemeWidgetFactory(WidgetFactory):

    def getButton(self):
        return DarkThemeButton()

    def getAlert(self):
        return DarkThemeAlert()


themeFactory = DarkThemeWidgetFactory()

button = themeFactory.getButton()
button.name = 'Click me'

alert = themeFactory.getAlert()
alert.txt = 'Your OS is gone'


print(button)
print(alert)
