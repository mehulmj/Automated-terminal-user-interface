import analytics
import os
import webcontroller
import weboperations
import osoperations
from flask import jsonify,Flask,request
os.system("systemctl stop firewalld")
app=Flask(__name__)
@app.route('/os')
def get_os_stats():
	battery_info=analytics.get_battery()
	ram_info=analytics.getram()
	login_info=analytics.login_info()
	running_process=osoperations.get_running_processes()
	return jsonify({'battery':battery_info, 'ram' : ram_info,'login':login_info,'running_process':running_process["running_processes"]})
@app.route('/webserver')
def get_webserver():
	list_of_files_html=webcontroller.list_files_html()
	list_of_files_cgi=webcontroller.list_files_cgi()
	status = webcontroller.web_status()
	home_page=webcontroller.get_home_html()
	return jsonify({'list_files_html' : list_of_files_html,'list_files_cgi' : list_of_files_cgi,'status': status,'home_page_html':home_page})
@app.route('/osoperations/check_software')
def check_software():
	software_name= request.args.get("software_name")
	check=osoperations.check_software(software_name)
	return jsonify(check)
@app.route('/osoperations/install_software')
def install_software():
	software_name= request.args.get("software_name")
	check=osoperations.install_software(software_name)
	return jsonify(check)
@app.route('/osoperations/install_software')
def uninstall_software():
	software_name= request.args.get("software_name")
	check=osoperations.uninstall_software(software_name)
	return jsonify(check)
@app.route('/osoperations/get_running_process')
def running_processes():
	process=osoperations.get_running_processes()
	return jsonify(process)
@app.route('/osoperations/directory_content')
def get_directory():
	directory= request.args.get("directory") or "/"
	response=osoperations.get_list_files_dir(directory)
	return jsonify(response)
@app.route('/weboperations/delete_file_html')
def delete_file_html():
	file_name=request.args.get("file_name")
	response=weboperations.delete_file_html(file_name)
	return jsonify(response)

@app.route('/weboperations/delete_file_cgi')
def delete_file_cgi():
	file_name=request.args.get("file_name")
	response=weboperations.delete_file_cgi(file_name)
	return jsonify(response)
@app.route('/weboperations/rename_file_html')
def rename_file_html():
	file_name=request.args.get("file_name")
	to_name=request.args.get("to_name")
	response=weboperations.rename_file_html(file_name,to_name)
	return jsonify(response)

@app.route('/weboperations/rename_file_cgi')
def rename_file_cgi():
	file_name=request.args.get("file_name")
	to_name=request.args.get("to_name")
	response=weboperations.rename_file_cgi(file_name,to_name)
	return jsonify(response)
@app.route('/weboperations/stop_server')
def stop_server():
	response=weboperations.stop()
	return jsonify(response)
@app.route('/weboperations/start_server')
def start_server():
	response=weboperations.start()
	return jsonify(response)
@app.route('/weboperations/reboot_server')
def reboot_server():
	response=weboperations.reboot()
	return jsonify(response)
@app.route('/weboperations/check_status')
def check_status_server():
	response=weboperations.check_status()
	return jsonify(response)
app.run(host='192.168.43.172')
	
