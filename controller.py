import analytics

from flask import jsonify,Flask
app=Flask(__name__)
@app.route('/')
def get_api():
	battery_info=analytics.get_battery()
	ram_info=analytics.getram()
	login_info=analytics.login_info()
	running_process=analytics.current_process()
	return jsonify({'battery':battery_info, 'ram' : ram_info,'login':login_info,'running_process':running_process})
app.run(host='0.0.0.0')
	
