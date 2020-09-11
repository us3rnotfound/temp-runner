import curses
import string
import time
import config_parser as config

class Config():
    
    def __init__(self):
        self.config_list = config.read_config()
        self.quit = False
    
    def main(self, stdscr):
        while self.quit == False:
            stdscr.clear()
            stdscr.timeout(2000)
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

            while self.quit == False:
                choice = self.curses_input(stdscr, 8,0,"Select Option 1 - 3 using a USB keyboard: ", True)
                if choice == '1':
                    units = 'A'
                    while self.quit == False and units.upper() != 'C' and units.upper() != 'F' and units.upper() != 'Q':
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
                    while max_limit.isdigit() == False and max_limit.upper() != 'Q':
                        if max_limit.isdigit() == False:
                            stdscr.clrtoeol()
                        max_limit = self.curses_input(stdscr, 8,0,"Type the new max limit temperature in °"+self.config_list['units']+", or type 'Q' + Enter to go back: ")
                        
                    if max_limit.upper() == 'Q':
                        break
                    else:
                        self.config_list['max_limit'] = float(max_limit)
                        self.save_config(stdscr)
                        break
                
                elif choice == '3':
                    names = ['','','','','']
                    for n in range(1,6):
                        stdscr.clrtoeol()
                        name = self.config_list['sensor_'+str(n)+'_name']
                        name = self.curses_input(stdscr, 8,0,"Type in new name to replace \"" + name + "\", or type 'Q' + Enter to go back: ")
                        if name.upper() == 'Q' or self.quit:
                            break
                        names[n-1] = name
                    
                    if self.quit == False and name.upper() != 'Q':
                        for n in range(1,6):
                            self.config_list['sensor_'+str(n)+'_name'] = names[n-1]
                        self.save_config(stdscr)
                    break
        curses.endwin

    def save_config(self,stdscr):
        config.write_config(self.config_list)  
        curses.noecho()
        stdscr.erase()
        try:
            stdscr.addstr(1, 0, "SETTINGS SAVED! PULL CONFIG JUMPER TO GO BACK TO RUN MODE")
        except:
            pass
        stdscr.refresh()
        curses.napms(5000)
    
    def curses_input(self, stdscr, row, col, prompt_string, ascii_mode=False):
        """
        Get an input string with curses.

        Row and col are the start position ot the prompt_string.
        """
        
        stdscr.addstr(row, col, str(prompt_string), curses.A_REVERSE)
        #stdscr.addstr(row + 1, col, " " * (curses.COLS - 1))
        stdscr.refresh()
        input_val = ""

        while self.quit == False:
            if ascii_mode:
                curses.noecho()
                input_val = stdscr.getch()
                if input_val != -1:
                    input_val = chr(input_val)
                    break
            else:
                curses.echo()
                input_val = self.get_str(stdscr, 20)
                break
                
    
        return input_val 

    def get_str(self, stdscr, return_len):
        word = ''
        while self.quit == False and len(word) <= return_len:
            ch = stdscr.getch()
            if ch != -1:
                if ch == 10:
                    break
                else:
                    word += chr(ch)
        return word

    def run(self):
        self.quit = False
        curses.wrapper(self.main)
        
    def stop(self):
        self.quit = True

if __name__ == "__main__":
    c = Config()
    c.run()