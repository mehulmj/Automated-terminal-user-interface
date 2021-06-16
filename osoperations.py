import os
import subprocess

def check_software(software_name):
	p = subprocess.Popen(["rpm","-q",software_name], stdout=subprocess.PIPE)
	out, err = p.communicate()
	out=str(out)
	response={}
	if("not installed" in out):
		response["software_exists"]=False
	else:
		response["software_exists"]=True
		response["software_name"]=out[2:len(out)-3]
	return response
def install_software(software_name):
	install_cmd="dnf install " + software_name
	os.system(install_cmd)
	response={}
	check=check_software(software_name)
	if(check["software_exists"]==True):
		response["installation"]=True
	else:
		response["installation"]=False
	return response
def uninstall_software(software_name):
	uninstall_cmd="yum remove " + software_name
	os.system(uninstall_cmd)
	response={}
	check=check_software(software_name)
	if(check["software_exists"]==True):
		response["installation"]=False
	else:
		response["installation"]=True
	return response
def get_list_files_dir(directory="/"):
	p = subprocess.Popen(["ls",directory], stdout=subprocess.PIPE)
	out, err = p.communicate()
	out=str(out)[2:].split("\\n")
	p = subprocess.Popen(["ls",directory,"-g"], stdout=subprocess.PIPE)
	put, err = p.communicate()
	put=str(put)[2:]
	put=str(put)[2:].split("\\n")
	file_type=[]
	response={}
	for i in range(len(put)-2):
		ftype="dir"
		if(put[i].split()[0][0] == '-'):
			ftype="file"
		file_type.append({"name":out[i],"file_type":ftype})
	response["list_of_files"]=file_type
	return response
def get_running_processes():
	p = subprocess.Popen(["ps","-aux"], stdout=subprocess.PIPE)
	out, err = p.communicate()
	out=str(out)[2:].split("\\n")
	headers=["USER","PID","%CPU","%MEM","VSZ","RSS","TTY","STAT","START","TIME","COMMAND"]
	process_list=[]
	for i in range(len(out)-2):
		temp={}
		put=out[i].split()
		for j in range(len(headers)-1):
			temp[headers[j]]=put[j]
		cmd=""	
		for j in range(j+1,len(put)):
			cmd += put[j]
		temp["COMMAND"]=cmd
		process_list.append(temp)
	response={}
	response["running_processes"]=process_list
	return response
