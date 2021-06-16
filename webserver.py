import subprocess
import ui_design
import os
import time
#------------------------------------------------------------------------
#header
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
	print("WEB SERVER",end="")
	for i in range(int(int(temp[1])/2),int(temp[1])-10):
		print(' ',end="")	
	ui_design.reset()
	ui_design.background(7)
	ui_design.color(2)
	for i in range(int(temp[1])):
		print('-',end="")
	ui_design.reset()
#------------------------------------------------------------------------
#checking software requirement
def software_requirement():
	if(subprocess.run(["rpm","-q","httpd"],stdout=subprocess.DEVNULL).returncode==1):
		ui_design.color(1)
		print("!Apache web server not installed",end=" ")
		print(u'\u2717')
		ui_design.reset()
		print("installing web server")
		subprocess.run(["yum","install","httpd","-y"],stdout=subprocess.DEVNULL)
	ui_design.color(2)
	print("Apache web server is installed",end=" ")
	print(u'\u2713')
	if(subprocess.run(["systemctl","status","firewalld"],stdout=subprocess.DEVNULL).returncode==0):
		ui_design.color(1)
		print("!Firewall is enabled, firewall must be disabled for web server to work",end=" ")
		print(u'\u2717')
		os.system("systemctl stop firewalld")

	ui_design.color(2)
	print("Firewall disabled ",end="")
	print(u'\u2713')	
	os.system("systemctl enable httpd")
	print("Httpd enabled ",end="")
	print(u'\u2713')
	print("All requirements checked (3/3)",end=" ")
	print(u'\u2713\u2713\u2713')
	ui_design.reset()
#----------------------------------------------------------------------
def upload():
	os.system("clear")
	ui_design.color(3)
	print("Upload your files here")
	print("-----------------------")
	ui_design.reset()
	print("Enter the location where your files are located")
	files=input()
	inp="cp "
	inp+=files
	inp+=" /var/www/html"
	os.system(inp)
	ui_design.color(5)
	print("Want to upload more files?(y/n)")
	if(input()=="y"):
		upload()
#----------------------------------------------------------------------
def list_files():
	os.system("clear")
	ui_design.color(3)
	print("THe list of files in the web server: ")
	ui_design.reset()
	os.system("ls /var/www/html")
	time.sleep(10)
	web_menu()

#----------------------------------------------------------------------
def homepage():
	for i in range(3):
		if i==0:
			ui_design.color(1)
		elif i==1:
			ui_design.color(3)
		else:
			ui_design.color(2)
		print("You are going to see the home page in a few seconds:")
		time.sleep(2)
	os.system("xdg-open http://0.0.0.0")
	webserver_main()
#----------------------------------------------------------------------
def change_port():
	ui_design.color(3)
	print("Change the port number")
	print("----------------------")
	ui_design.reset()
	print("The file with the configuration is going to open in 10 seconds ")
	print("You can change the port number, you will get the field when the file opens..")
	ui_design.color(3)
	print("Listen xyz....Replace xyz with the port number of your choice")
	print("The current port number is")
	os.system("netstat -tlnp|grep httpd")
	ui_design.reset()
	print("	Please save the file after changing the port number")
	print()
	time.sleep(10)
	os.system("gedit /etc/httpd/conf/httpd.conf")
	print("Have you updated?(y/n)")
	if(input()=="y"):
		print("please wait while we update the port number for you")
		os.system("systemctl restart httpd")
		time.sleep(3)
		print("The new port number is:")
		os.system("netstat -tlnp | grep httpd")
		time.sleep(4)
	web_menu()		
#---------------------------------------------------------------------
def view_connection():
	print(os.system("cat /etc/httpd/logs/access_log"))
	for _ in range(31000000):
		continue
	print("Return?(y/n)")
	if(input()=='y'):
		web_menu()
	else:
		view_connection()
			
#----------------------------------------------------------------------
#main menu for web server
def web_menu():
	while(True):
		os.system("clear")
		header()
		print("What do you want to do?")
		print("1)Upload a file in the web server")
		print("2)List of files in the web server")
		print("3)View the home page")
		print("4)Change the port number")
		print("5)View who connnected to you?")
		print("6)Return to the main menu?")
		ch=int(input())
		if(ch==1):
			upload()
		elif(ch==2):
			list_files()
		elif(ch==3):
			homepage()		
		elif(ch==4):
			change_port()
		elif(ch==5):
			view_connection()
		elif(ch==6):
			import menu				
						
#--------------------------------------------------------------------------
def webserver_main():
	os.system("clear")
	header()
	software_requirement()
	for _ in range(31000000):
		continue
	os.system("clear")
	web_menu()

