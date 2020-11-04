import subprocess
import ui_design
import os
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
#main menu for web server

def menu():
	while(True):
		#os.system("clear")
		header()
		print("What do you want to do?")
		print("1)Upload a file in the web server")
		print("2)List of files in the web server")
		print("3)View the home page")
		print("4)Change the port number")
		print("5)Return back to the home screen")
		ch=int(input())
		if(ch==2):
			temp=subprocess.run(["ls","/var/www/html"],stdout=subprocess.PIPE).stdout
			temp=str(temp)
			temp=temp[2:]
			temp=temp.split('\\n')
			for i in range(len(temp)-1):
				print(temp[i])
					
		
#--------------------------------------------------------------------------
def main():
	os.system("clear")
	header()
	software_requirement()
	for _ in range(31000000):
		continue
	os.system("clear")
	menu()
