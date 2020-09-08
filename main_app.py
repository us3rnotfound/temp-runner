from fsm import fsm
from gpiozero import Button
from signal import pause
from threading import Thread
import time
import termios, sys , tty

# UNITS:
F = 0
C = 1

class Temp_runner():
    
    def __init__(self):
        self.fsm = fsm()

        config_pin = Button(21)
        config_pin.hold_time = 2 # seconds

        config_pin.when_held = self.to_config_state
        config_pin.when_released = self.to_run_state

        if config_pin.value:
            self.to_config_state()
        else:
            self.to_run_state()

    def to_run_state(self):
        thread = Thread(target=self.fsm.to_run_state)
        thread.start()
        time.sleep(0.01) # thread requires some time to start

    def to_config_state(self):
        thread = Thread(target=self.fsm.to_config_state)
        thread.start()
        time.sleep(0.01) # thread requires some time to start

    def key_watch(self):
        while True:
            print ("Enter c or r: ")
            key = self._getch()
            if key=='c':
                print (key)
                self.fsm.trigger_configure()
            elif key=='r':
                print (key)
                self.fsm.trigger_run()
            else:
                return
                

    def _getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)     #This number represents the length
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


t = Temp_runner()

pause()