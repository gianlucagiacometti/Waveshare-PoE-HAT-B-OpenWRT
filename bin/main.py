import time
import sys
import os
import json

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
cfgdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'cfg')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging

from waveshare_POE_HAT_B import POE_HAT_B

 
logging.basicConfig(level=logging.INFO)

POE = POE_HAT_B.POE_HAT_B()

f = open(cfgdir + "/options.json", "r")
config = json.load(f)
fan_temp = config["fan_temp"]
"""
delta_temp = config["delta_temp"]
sleep_duration = config["sleep_duration"]
"""
f.close()
        
try:  
    while(1):
        POE.POE_HAT_Display(fan_temp)
        time.sleep(1)
        
except KeyboardInterrupt:    
    print("ctrl + c:")
    POE.FAN_OFF()
  
