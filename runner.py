
from video_output import Video_output
from read_temps_class import Read_temps

F = 0
C = 1

class Runner():    
    def __init__(self, units=F):
        self.units = units
        self.therm = Read_temps()
        self.v = Video_output()

    def _get_temps(self):
        t_c_list, t_f_list = self.therm.read_temp()
        if self.units == F:
            return t_f_list
        else:
            return t_c_list
        
    def output_temps(self):
        self.v.update_temps(self._get_temps()):

    def loop(self, times_to_run=0):
        t = 0
        while True:
            t+= 1
            self.r.output_temps()
            if t == times_to_run:
                break
        return

if __name__ == "__main__":
    r = Runner(F)
    r.loop(0)
