from interface import Device


class Controller:
    """Контроллер
    """
    
    def __init__(self,device:Device):
        self.device = device
    
    def __str__(self):
        if self.device:
            return f"Контроллер подключен к {self.device.name}"
        else:
            return "Контроллер не подключен"