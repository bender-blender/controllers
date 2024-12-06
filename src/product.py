from interface import Device
from controller import Controller


class Xbox(Device):
    """Xbox

    Args:
        Device (_type_): _description_
    """
    
    def __init__(self):
        self.name = "Xbox"
        self.periphery = Controller(self)



class PS(Device):
    """Playstation

    Args:
        Device (_type_): _description_
    """
    def __init__(self):
        self.name = "Playstation"
        self.periphery = Controller(self)


class Computer(Device):
    """Компютер

    Args:
        Device (_type_): _description_
    """
    def __init__(self,periphery):
        self.name = "Компютер"
        self.periphery = periphery
        if self.periphery is Controller:
            print("Нельзя подключить")
            self.periphery = None
        else:
            print(f"{self.periphery} подключена к Компютеру")


