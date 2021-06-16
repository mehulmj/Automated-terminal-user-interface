import os
import subprocess
import ui_design
import time
import gnuplotlib as gb
import numpy as np

#----------------------------------------------------------------------------
def header():
	temp=os.popen('stty size','r').read().split()
	ui_design.background(5)
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
def login_info():
	val=str(subprocess.run(["w"],stdout=subprocess.PIPE))
	val=val.split("\\n")
	header=[]
	head=val[1].split()
	for i in range(4):
		header.append(head[i])
	login=[]
	for i in range(2,len(val)-1):
		temp={}
		tempval=val[i].split()
		for j in range(4):
			temp[header[j]]=tempval[j]
		login.append(temp)
	return login
#----------------------------------------------------------------------------
def current_process():
	val=str(subprocess.run(["ps"],stdout=subprocess.PIPE))
	val=val.split("\\n")
	header=[]
	head=val[0].split()
	for i in range(1,len(head)):
		header.append(head[i])
	running_process=[]
	for i in range(1,len(val)-3):
		temp={}
		tempval=val[i].split()
		for j in range(4):
			temp[header[j]]=tempval[j]
		running_process.append(temp)
	return running_process
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
	batt=[get_battery()]*1000
	y=[i for i in range(0,100)]
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
		print(batt[len(batt)-1])
		os.system("clear")
		time.sleep(1)
#----------------------------------------------------------------------------
def getram():
	val=str(subprocess.run(["free","-m"],stdout=subprocess.PIPE))
	val=val.split("available")
	val=val[1].split()
	total=int(val[1])
	free=int(val[3])
	return free
#----------------------------------------------------------------------------
def ram():
	free=[0]*100
	y=[i for i in range(0,100)]
	while(True):
		os.system("clear")
		free.append(getram())
		free.pop(0)
		ui_design.color(3)

		gb.plot(np.array(y),np.array(free),terminal="dumb",_with='lines',unset='grid')							
		ui_design.reset()
		print(free[len(free)-1])
		os.system("clear")
		time.sleep(5)
	
#----------------------------------------------------------------------------
def menu_analytics():
	while(True):
		os.system("clear")
		header()
		ui_design.color(3)
		print("Select one of the options from below:")
		ui_design.reset()
		print("1)Battery")
		print("2)Ram")
		print("3)Storage")
		print("4)Retrurn to the menu")
		print("5)Exit")
		print("Enter your choice: ",end=" ")
		ch=int(input())
		print()
		os.system("clear")
		if(ch==1):
			battery()
		elif(ch==2):
			ram()
		elif(ch==3):
			storage()
		elif(ch==4):
			import menu
		elif(ch==5):
			break	
		else:
			print("Invalid input")
	
	
#----------------------------------------------------------------------------

