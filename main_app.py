from fsm import fsm
from gpiozero import Button
from signal import pause
import threading
import termios, sys , tty

# UNITS:
F = 0
C = 1

class Temp_runner():
    
    def __init__(self):
        self.fsm = fsm()

        self.x = threading.Thread(target=self.key_watch)
        self.x.start()

        #config_pin = Button(21)
        #config_pin.hold_time = 2 # seconds

        #config_pin.when_held = self.fsm.trigger_configure
        #config_pin.when_released = self.fsm.trigger_run

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