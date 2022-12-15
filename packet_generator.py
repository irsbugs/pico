import random
from machine import Timer, ADC
import time
import sys
tim = Timer()
#print(dir(random))
# ['__class__', '__init__', '__name__', '__dict__', 'choice',
#'getrandbits', 'randint', 'random', 'randrange', 'seed',
#'uniform']

#reading = ""
stamp = time.time()
reading_dict = {stamp:[]}
#count = 0
temp_sensor = machine.ADC(4)

def cb_add_data(timer, count): #, stamp):
    #print(dir(timer))
    # ['__class__', '__del__', 'ONE_SHOT', 'PERIODIC', 'deinit',
    #'init']
    global reading_dict
    #global count
    global stamp
    global temp_sensor
    count += 1
                
    #reading = random.randint(0, 4096)
    reading = temp_sensor.read_u16()
    reading_dict[stamp].append(reading)
    #print("tick")
    
    if stamp + 1 == time.time():
        # A second has gone buy
        print(reading_dict)
        print(len(reading_dict[stamp]))
        
        stamp = time.time()
        reading_dict = {stamp:[]}
                
    #print(reading_dict)
    if count == 200:
        tim.deinit()
        sys.exit()

if __name__=="__main__":
    count = 0
    #stamp = time.time()
    #tim.init(freq=50, mode=Timer.PERIODIC, callback=(cb_add_data, count))
    #callback = lambda pin: toggle_led(), Pin.IRQ_RISING
    
    callback = (lambda temp_sensor: cb_add_data(Timer, count)) #, stamp))   #, count)
    
    tim.init(freq=50, mode=Timer.PERIODIC, callback=callback)
    
    #tim.init(freq=50, mode=Timer.PERIODIC, callback=(cb_add_data))    
"""
{1671135670: [2379, 2472, 1732, 129]}
{1671135671: [109, 1147, 1451, 2379, 3476]}
{1671135672: [440, 3832, 1313, 1326, 3869]}
{1671135673: [2448, 1541, 2738, 1578, 258]}
Traceback (most recent call last):

50
{1671138877: [14147, 14163, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14131, 14131, 14147, 14147, 14147, 14147, 14131, 14147, 14147, 14147, 14147, 14147, 14131, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14131, 14147, 14147, 14147, 14147, 14147]}
50
{1671138878: [14163, 14147, 14147, 14147, 14147, 14131, 14147, 14147, 14147, 14147, 14147, 14163, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14131, 14147, 14147, 14147, 14147, 14147, 14131, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14131, 14131, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14147, 14131, 14147]}
50

"""
