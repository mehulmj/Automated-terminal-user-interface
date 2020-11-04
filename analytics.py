import os
import subprocess
import ui_design
import time
import gnuplotlib as gb
import numpy as np

#----------------------------------------------------------------------------
def header():
	temp=os.popen('stty size','r').read().split()
	ui_design.background(7)
	ui_design.color(2)
	for i in range(int(temp[1])):
		print('-',end="")
	for i in range(int(int(temp[1])/2)):
		print(' ',end="")

	ui_design.blink_text()
	ui_design.bold()
	print("ANALYTICS",end="")
	for i in range(int(int(temp[1])/2),int(temp[1])-9):
		print(' ',end="")	
	ui_design.reset()
	ui_design.background(7)
	ui_design.color(2)
	for i in range(int(temp[1])):
		print('-',end="")
	ui_design.reset()

#----------------------------------------------------------------------------
def get_battery():
	val=str(subprocess.run(["upower","-i","/org/freedesktop/UPower/devices/battery_BAT0"],stdout=subprocess.PIPE))
	val=val.split("percentage")
	val=val[1].split("\\n")
	val=val[0].split(":")[1]
	for i in range(len(val)):
		if(val[i]!=''):
			break
	val=val[i:len(val)-1]
	return int(val)
#----------------------------------------------------------------------------
def battery():
	batt=[get_battery()]*100
	y=[i for i in range(0,100)]
	os.system("clear")
	while(True):
		os.system("clear")
		batt.append(get_battery())
		batt.pop(0)
		if(batt[len(batt)-1]>60):
			ui_design.color(2)
		elif(batt[len(batt)-1]>30):
			ui_design.color(4)
		else:
			ui_design.color(1)
		gb.plot(np.array(batt),terminal="dumb",_with='lines',unset='grid')							
		ui_design.reset()
		os.system("clear")
		time.sleep(6)
#----------------------------------------------------------------------------
def menu_analytics():
	header()
	battery()
	
#----------------------------------------------------------------------------
menu_analytics()
