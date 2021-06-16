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
	time.sleep(4)
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
def launch():
	os.system("clear")
	ui_design.color(3)
	print("Welcome to the container launch window!!")
	print("-----------------------------------------")
	ui_design.reset()
	print("Enter the name of the container you want to launch:")
	name=input()
	print("Enter the name of the os image:")
	osimage=input()
	inp="docker run -it --name "
	inp+=name
	inp+=" " +osimage
	os.system(inp)
	print("Want to launch another container?(y/n)")
	if(input()=="y"):
		launch()
	else:
		docker_main()
#--------------------------------------------------------------------------
def show_running():
	ui_design.color(3)
	print("Here you can see the running containers")
	print("----------------------------------------")
	ui_design.reset()
	os.system("docker container ls --all")
	time.sleep(6)
	docker_menu()
#--------------------------------------------------------------------------
def images_list():
	ui_design.color(3)
	print("Here you can see the running containers")
	print("----------------------------------------")
	ui_design.reset()
	os.system("docker images ls --all")
	time.sleep(6)
#--------------------------------------------------------------------------
def docker_menu():
	os.system("clear")
	ui_design.color(3)
	print("Here's what you can do:")
	ui_design.reset()
	print()
	print("1)Start a container")
	print("2)Show the list of running containers")
	print("3)Show the available images")
	print("4)Show configuration")
	print("5)Return to the main menu?")
#--------------------------------------------------------------------------
def docker_main():
	requirement()
	time.sleep(0.8)
	os.system("clear")
	while(True):
		docker_menu()
		ch=int(input())
		if(ch==1):
			launch()
		elif(ch==2):
			show_running()
		elif(ch==3):
			images_list()
		elif(ch==4):
			configuration()
		else:
			import menu
