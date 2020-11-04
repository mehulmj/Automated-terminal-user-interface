import docker
import os
import subprocess
import ui_design
import time
import sample
#------------------------------------------------------------------------
#checking software requirement
def requirement():
	if(subprocess.run(["rpm","-q","docker-ce"],stdout=subprocess.DEVNULL).returncode==1):
		ui_design.color(1)
		print("Docker not installed",end="")
		print(u'\u2717')
		ui_design.reset()
		print("installing docker")
		os.system("sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
		os.system("sudo dnf install https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.6-3.3.el7.x86_64.rpm")
		os.system("sudo dnf install docker-ce")
	ui_design.color(2)
	print("Docker is installed",end=" ")
	print(u'\u2713')
	print("Required packages installed",end=" ")
	print(u'\u2713\u2713')	
	ui_design.reset()
#--------------------------------------------------------------------------
def header():
	temp=os.popen('stty size','r').read().split()
	ui_design.background(7)
	os.system("tput setab 7")
	ui_design.color(2)
	for i in range(int(temp[1])):
		print('-',end="")
	for i in range(int(int(temp[1])/2)):
		print(' ',end="")
	ui_design.blink_text()
	ui_design.bold()
	print("DOCKER",end="")
	for i in range(int(int(temp[1])/2),int(temp[1])-10):
		print(' ',end="")	
	ui_design.reset()
	ui_design.background(7)
	ui_design.color(2)
	for i in range(int(temp[1])):
		print('-',end="")
	ui_design.reset()
#--------------------------------------------------------------------------
def menu():
	os.system("clear")
	print("Here's what you can do:")
	print("1)Start a container")
	print("2)Show the list of running containers")
	print("3)Show the available images")
	print("4)Show configuration")
	print("5)Return back to the main menu")
#--------------------------------------------------------------------------
if __name__=="__main__":
	requirement()
	time.sleep(0.8)
	os.system("clear")
	while(True):
		menu()
		ch=int(input())
		if(ch==1):
			launch()
		elif(ch==2):
			containerlist()
		elif(ch==3):
			imageslist()
		elif(ch==4):
			configuration()
		else:
			sample.main()
