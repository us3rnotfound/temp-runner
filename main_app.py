from fsm import fsm
from gpiozero import Button
from signal import pause
from threading import Thread
import time
#import termios, sys , tty

class Temp_runner():
    
    def __init__(self):
        self.fsm = fsm()

        self.config_pin = Button(21, pull_up=True, bounce_time=1)

        #self.config_pin.when_held = self.to_config_state
        #self.config_pin.when_released = self.to_run_state

    def run(self):
        while True:
            '''
            self.to_run_state()

            time.sleep(10)

            self.to_config_state()

            time.sleep(20)
            '''
            
            if self.config_pin.value:
                if self.fsm.state != 'config_state':
                    self.to_config_state()
            else:
                if self.fsm.state != 'run_state':
                    self.to_run_state()
        
            time.sleep(2)
            
    def to_run_state(self):
        self.run_thread = Thread(target=self.fsm.to_run_state)
        self.run_thread.start()
        time.sleep(0.01) # thread requires some time to start

    def to_config_state(self):
        self.config_thread = Thread(target=self.fsm.to_config_state)
        self.config_thread.setDaemon(True)
        self.config_thread.start()
        time.sleep(0.01) # thread requires some time to start


t = Temp_runner()
t.run()