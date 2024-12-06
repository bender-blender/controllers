
from product import (
    Xbox,
    PS,
    Computer
)

from interface import Device
from adapter import Adapter
def client_code(product:Device):
    adapter = Adapter(product)
    adapter.connect_the_controller()

client_code(Xbox())
client_code(PS())
computer = Computer("Мышь")
client_code(computer)