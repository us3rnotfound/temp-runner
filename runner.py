
from video_output import Video_output
from read_temps_class import Read_temps

F = 0
C = 1

class Runner():    
    def __init__(self, units=F, max_limit=80):
        # Parameters
        self.units = units
        self.max_limit = max_limit
        self.quit = False

        # Module inits
        self.therm = Read_temps()
        self.v = Video_output()
        
    def _get_temps(self):
        t_c_list, t_f_list = self.therm.read_temp()
        over_limit_list_c = [t > self.max_limit for t in t_c_list]
        over_limit_list_f = [t > self.max_limit for t in t_f_list]

        if self.units == F:
            return t_f_list, over_limit_list_f
        else:
            return t_c_list, over_limit_list_c

    def loop(self, times_to_run=0):
        t = 0
        while self.quit == False:
            t+= 1
            temps_list, over_limit_list = self._get_temps()
            self.v.update_temps(temps_list, over_limit_list)
            if t == times_to_run:
                break
        
        # Quit goes True or times to run exceeded:
        self.v.destroy_video()

    def stop_running(self):
        print ('trying to quit (runner)')
        self.quit = True
        
if __name__ == "__main__":
    r = Runner(units=F)
    r.loop(5)
