from interface import Device
from controller import Controller

class Adapter:
    """Адаптер
    """

    def __init__(self,device:Device):
        self.device = device

    def connect_the_controller(self):
        """Присойденить контроллер
        """
        if self.device.periphery is not Controller:
            self.device.periphery = Controller(self.device.name)
            print(f"Контроллер подключен к {self.device.name}")
        else:
            print(f"Контроллер уже подключен к {self.device.name}")
