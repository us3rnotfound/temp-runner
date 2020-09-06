from fsm import fsm
from gpiozero import Button
from signal import pause

# UNITS:
F = 0
C = 1

class Temp_runner():
    
    def __init__(self):
        self.fsm = fsm()

        config_pin = Button(21)
        config_pin.hold_time = 2 # seconds
        config_pin.when_held = self.fsm.trigger_configuring
        config_pin.when_released = self.fsm.trigger_running

t = Temp_runner()

pause()