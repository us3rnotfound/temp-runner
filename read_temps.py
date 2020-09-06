import os
import glob
import time
from w1thermsensor import W1ThermSensor

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_folders = glob.glob(base_dir + '28*')
device_file = device_folder + '/w1_slave'
device_files = [df + '/w1_slave' for df in device_folders]

def read_temp_raw(df):
    f = open(df, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    temp_c_list = []
    temp_f_list = []
    for df in device_files:
        lines = read_temp_raw(df)
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.1)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_c_list.append(temp_c)
            temp_f_list.append(temp_c * 9.0 / 5.0 + 32.0)
    return temp_c_list, temp_f_list

while True:
    print(read_temp())
    time.sleep(1)
