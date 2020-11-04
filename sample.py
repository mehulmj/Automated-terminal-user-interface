import gnuplotlib as gb
import numpy as np
import subprocess
import time
import os



val=str(subprocess.run(["upower","-i","/org/freedesktop/UPower/devices/battery_BAT0"],stdout=subprocess.PIPE))
val=val.split("percentage")
val=val[1].split("\\n")
val=val[0].split(":")[1]
for i in range(len(val)):
	if(val[i]!=''):
		break
val=val[i:len(val)-1]
print(int(val))	
