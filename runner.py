
from video_output import Video_output
from read_temps_class import Read_temps

F = 0
C = 1

class Runner():    
    def __init__(self, units=F):
        self.units = units
        self.therm = Read_temps()
        self.v = Video_output()
        self.quit = False

    def _get_temps(self):
        t_c_list, t_f_list = self.therm.read_temp()
        if self.units == F:
            return t_f_list
        else:
            return t_c_list

    def loop(self, times_to_run=0):
        t = 0
        while self.quit == False:
            t+= 1
            self.v.update_temps(self._get_temps())
            if t == times_to_run:
                self.v.destroy_video()
                break

    def stop_running(self):
        self.quit = True
        

if __name__ == "__main__":
    r = Runner(units=F)
    r.loop(5)
