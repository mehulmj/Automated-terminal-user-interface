import os 
import os.path
import getpass #used for hidden password
import ui_design
import docker as dc
import analytics
import webserver
#--------------------------------------------------------------------------------------
#Header function
def header():
	ui_design.background(7)
	ui_design.color(0)
	print("                                                                       ",end=" ")
	print("        ")
	print("------------------------------------------------",end="")
	print("--------------------------------")
	ui_design.blink_text()
	ui_design.bold()
	print("                                  WELCOME TO ATUI                               ")
	ui_design.reset()
	ui_design.background(7)
	ui_design.color(0)
	print("------------------------------------------------",end="")
	print("--------------------------------")
	ui_design.reset()
#--------------------------------------------------------------------------------------
#function for the main menu

def menu():
	header()
	ui_design.color(3)
	print("\nWhat do you want to do?")
	ui_design.color(7)
	print("Work on remote(1)/local(0) system?")
	if(int(input())==1):
		print("Provide the login details of the remote system..")
		print("username: ",end=" ")
		username=input()
		print()
		password=getpass.getpass()
	print("1)Install any software")
	print("2)Configure Web Server")
	print("3)Work with Docker")
	print("4)Analytics")
	print("5)View previous logins to the system")

#------------------------------------------------------------------------------
#function for software installation
def yum():
	print("Enter the name of the software you want to install: ",end="")
	os.system("yum install {}".format(input()))
	print("Press (1) to install any other software?")
	print("Press (2) to return back")
	if(input()==1):
		yum()
#---------------------------------------------------------------------------------
#Previous login	
def prevlogin():
	os.system("clear")
	header()	
	print(os.system("w"))
	ui_design.color(2)
	print("Want to check again?(Y to agree)")
	ui_design.reset()
	if(input()=='y' or input()=='Y'):
		prevlogin()
	else:
		return
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------	
#main
def menu_main():
	flag=0
	ui_design.color(3)
	entry=getpass.getpass()
	if(entry=="root"):
		flag=1
	if(flag==0):
		for i in range(3):
			if(i==0):ui_design.color(2)
			if(i==1):ui_design.color(3)
			if(i==2):ui_design.color(1)
			print("Enter the password again, Your have {} attempts left".format(3-i),end=" ") 
			if(i==0):
				print("\N{grinning face}")
			elif(i==1):
				print("\N{thinking face}")
			else:
				print("\N{face with thermometer}")
			ui_design.color(3)		
			entry=getpass.getpass()
			if(entry=="root"):
				flag=1
				break
	if(flag==1):
		#f=open("login.txt","w+")	
		ch=-1
		while(True):
			os.system("clear")
			menu()
			print("Enter your choice: ",end="")
			ch=input()
			if(ch=="1"):
				yum()
			if(ch=="2"):
				webserver.webserver_main()
			if(ch=="3"):
				dc.docker_main()
			if(ch=="4"):
				analytics.menu_analytics()
			elif(ch=="5"):
				prevlogin()
			else:
				print("Enter correct choice")
			os.system("clear")
		#os.remove("login.txt")
	ui_design.reset()
menu_main()

