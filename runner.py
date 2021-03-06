
from video_output import Video_output
from read_temps_class import Read_temps
import config_parser

class Runner():    
    def __init__(self):
        self.quit = False

        # Module inits
        self.therm = Read_temps()
        self.v = Video_output()
        
    def _get_temps(self):
        t_c_list, t_f_list = self.therm.read_temp()
        over_limit_list_c = [t > self.max_limit for t in t_c_list]
        over_limit_list_f = [t > self.max_limit for t in t_f_list]

        if self.units == 'F':
            return t_f_list, over_limit_list_f
        else:
            return t_c_list, over_limit_list_c

    def update_config(self):
        config_list = config_parser.read_config()
        self.units = config_list['units']
        self.max_limit = config_list['max_limit']
        self.sensor_name_list = [config_list['sensor_1_name'],
                                 config_list['sensor_2_name'],
                                 config_list['sensor_3_name'],
                                 config_list['sensor_4_name'],
                                 config_list['sensor_5_name']]
        print (config_list)

    def run(self, times_to_run=0):
        self.update_config()

        t = 0
        self.quit = False
        while self.quit == False:
            t+= 1
            temps_list, over_limit_list = self._get_temps()
            self.v.update_temps(temps_list, over_limit_list, self.sensor_name_list, self.units)
            if t == times_to_run:
                break
        
        # Quit goes True or times to run exceeded:
        self.v.destroy_video()

    def stop(self):
        print ('trying to quit (runner)')
        self.quit = True
        
if __name__ == "__main__":
    import time

    r = Runner()
    r.run(5)
