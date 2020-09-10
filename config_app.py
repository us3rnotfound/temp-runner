import curses
import string
import time
import config_parser as config

class InterruptExecution (Exception):
    pass

class Config():
    
    def __init__(self):
        self.config_list = config.read_config()
    
    def main(self, stdscr):
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "CONFIGURATION SETTINGS", curses.A_BOLD)
            stdscr.addstr(2, 0, "1. Units: ")
            if self.config_list['units'] == 'F':
                units = "Fahrenheit"
            else:
                units = "Celsius"
            stdscr.addstr(units)
            stdscr.addstr(3, 0, "2. Threshold Amplifier Shutdown Temperature: ")
            stdscr.addstr(str(self.config_list['max_limit']) + '°'+self.config_list['units'])
            stdscr.addstr(4, 0, "3. Sensor Display Names: ")
            stdscr.addstr(str([self.config_list['sensor_1_name'],
                               self.config_list['sensor_2_name'],
                               self.config_list['sensor_3_name'],
                               self.config_list['sensor_4_name'],
                               self.config_list['sensor_5_name']]))

            while True:
                choice = self.curses_input(stdscr, 8,0,"Select Option 1 - 3 using a USB keyboard: ", True)
                if choice == '1':
                    units = 'A'
                    while units.upper() != 'C' and units.upper() != 'F' and units.upper() != 'Q':
                        units = self.curses_input(stdscr, 8,0,"For Fahrenheit type 'F', for Celsius type 'C', or to go back type 'Q': ", True)
                    if units.upper() != self.config_list['units']:
                        
                        if units.upper() == 'Q':
                            break
                        else:
                            self.config_list['units'] = units.upper()
                            old_max_limit = self.config_list['max_limit']
                            # 'F' to 'C'
                            if self.config_list['units'] == 'C':
                                self.config_list['max_limit'] = round((old_max_limit - 32) * 5.0/9.0, 1)
                            # 'C' to 'F'
                            else:
                                self.config_list['max_limit'] = round(9.0/5.0 * old_max_limit + 32, 1)

                            self.save_config(stdscr)
                            break

                elif choice == '2':
                    max_limit = 'bad' # not a number
                    while max_limit.isdigit() == False and max_limit.upper() != b'Q':
                        max_limit = self.curses_input(stdscr, 8,0,"Type the new max limit temperature in °"+self.config_list['units']+", or type 'Q' + Enter to go back: ")
                        print (max_limit.upper())
                    if max_limit.upper() == b'Q':
                        break
                    else:
                        self.config_list['max_limit'] = float(max_limit)
                        self.save_config(stdscr)
                        break
                
                elif choice == '3':

                    break

    def save_config(self,stdscr):
        config.write_config(self.config_list)  
        curses.noecho()
        stdscr.addstr(10, 0, "SETTINGS SAVED! PULL CONFIG JUMPER TO GO BACK TO RUN MODE")
        stdscr.refresh()
        curses.napms(3000)
    
    def curses_input(self, stdscr, row, col, prompt_string, ascii_mode=False):
        """
        Get an input string with curses.

        Row and col are the start position ot the prompt_string.
        """
        curses.echo()
        stdscr.addstr(row, col, str(prompt_string), curses.A_REVERSE)
        stdscr.addstr(row + 1, col, " " * (curses.COLS - 1))
        stdscr.refresh()
        input_val = ""

        while len(input_val) <= 0:
            if ascii_mode:
                input_val = chr(stdscr.getch())
                break
            else:
                input_val = stdscr.getstr(row, len(prompt_string)+1, 20)

        return input_val 

    def run(self):
        try:
            curses.wrapper(self.main)
        except InterruptExecution:
            curses.endwin()

    def stop_running(self):
        raise (InterruptExecution('Stop Config'))

if __name__ == "__main__":
    c = Config()
    c.run()