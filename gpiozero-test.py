from gpiozero import Button
import time

config_pin = Button(21, pull_up=True, bounce_time=4, hold_time=1)

while True:
    if config_pin.is_held:
        print('ON')
    else:
        print('OFF')
    time.sleep(1)
    