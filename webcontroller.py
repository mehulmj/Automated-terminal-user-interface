import os 
import subprocess
import requests
def list_files_html():
	content=str(subprocess.run(["ls","/var/www/html"],stdout=subprocess.PIPE))
	content=content.split("stdout=b")[1].split("\\n")
	content=content[:len(content)-2]
	return content
def list_files_cgi():
	content=str(subprocess.run(["ls","/var/www/cgi-bin"],stdout=subprocess.PIPE))
	content=content.split("stdout=b")[1].split("\\n")
	content=content[:len(content)-1]
	return content
def get_home_html():
	os.system("systemctl start httpd")
	url = "http://localhost/"
	s = str(requests.get(url).content).split("\\n")
	s = ''.join(s).split("\\t")	
	s=''.join(s)
	return s

def web_status():
	url = "http://192.168.43.172/server-status?auto"
	s = str(requests.get(url).content).split("\\n")
	s=s[:len(s)-3]
	status={}
	for i in range(1,len(s)):
		temp=s[i].split(":")
		temp[1]=temp[1][1:]
		if(temp[1].isnumeric()):
			temp[1]=int(temp[1])
		elif(temp[1].replace('.', '', 1).isdigit()):
			temp[1]=float(temp[1])
		status[temp[0]]=temp[1]
	return status
