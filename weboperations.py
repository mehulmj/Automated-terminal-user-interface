import os
import subprocess

def check_status():
	p = subprocess.Popen(["systemctl","status","httpd"], stdout=subprocess.PIPE)
	out, err = p.communicate()
	out=str(out)
	response={}
	if("active (running)" in out):
		response["status"]=True
	else:
		response["status"]=False
	return response
def stop():
	os.system("systemctl stop httpd")
	status=check_status()
	if(status["status"]==True):
		return {"stop": False}
	else:
		return {"stop": True}
def start():
	os.system("systemctl start httpd")
	status=check_status()
	if(status["status"]==False):
		return {"start": False}
	else:
		return {"start": True}
def reboot():
	os.system("systemctl restart httpd")
	status=check_status()
	if(status["status"]==False):
		return {"reboot": False}
	else:
		return {"reboot": True}
def delete_file_html(file_name):
	os.system("rm /var/www/html/"+file_name)
	return {"delete":True}
def rename_file_html(file_name,new_file_name):
	os.system("mv /var/www/html/"+ file_name + " /var/www/html/"+ new_file_name)
	return {"rename":True}
def delete_file_cgi(file_name):
	os.system("rm /var/www/cgi-bin/"+file_name)
	return {"delete":True}
def rename_file_cgi(file_name,new_file_name):
	os.system("mv /var/www/cgi-bin/"+ file_name + " /var/www/cgi-bin/"+ new_file_name)
	return {"rename":True}	
