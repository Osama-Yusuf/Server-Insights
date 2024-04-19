from flask import Flask, render_template, jsonify
import psutil
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_resource_usage')
def get_resource_usage():
    # Simulate getting resource usage data
    cpu_usage = psutil.cpu_percent(interval=2)
    ram_usage = psutil.virtual_memory().percent
    storage_usage = psutil.disk_usage('/').percent

    # Read the host system's uptime from /proc/uptime
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    # Convert uptime to a more readable format (days, hours, minutes)
    days, seconds = divmod(int(uptime_seconds), 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    uptime_readable = f"{days} days, {hours:02}:{minutes:02}:{seconds:02}"

    return jsonify({
        'cpu_usage': cpu_usage,
        'ram_usage': ram_usage,
        'storage_usage': storage_usage,
        'uptime': uptime_readable
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
