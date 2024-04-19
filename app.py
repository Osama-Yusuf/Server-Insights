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

    # Fetch the EC2 instance type
    # check if the instance is running on EC2 if not give default value
    try:
        print("Running on EC2, fetching instance type")
        instance_type = subprocess.check_output("curl -s 169.254.169.254/latest/meta-data/instance-type", shell=True).decode("utf-8").strip()
    except:
        print("Not running on EC2, using default instance type")
        instance_type = "t3.large"

    # Define the hourly rates for the provided EC2 instance types
    hourly_rates = {
        't3.large': 0.0832,
        'c7g.xlarge': 0.1445,
        't4g.xlarge': 0.1344,
        'c7g.2xlarge': 0.289,
        'c6g.2xlarge': 0.272,
        't4g.2xlarge': 0.2688
    }

    # Calculate the cost based on the uptime and instance type
    if instance_type in hourly_rates:
        hourly_rate = hourly_rates[instance_type]
        uptime_hours = days * 24 + hours
        cost = uptime_hours * hourly_rate

        # Create a cost calculation details dictionary
        cost_details = {
            'total_hours': uptime_hours,
            'hourly_rate': hourly_rate,
            'cost_formula': f"Total Hours x Hourly Rate = {uptime_hours} hours x ${hourly_rate} = ${cost:.2f}"
        }

        cost_str = f"${cost:.2f}"  # Format cost as a string with two decimal places
    else:
        cost_details = {}
        cost_str = "$0.00"  # Default cost if instance type is not found

    return jsonify({
        'cpu_usage': cpu_usage,
        'ram_usage': ram_usage,
        'storage_usage': storage_usage,
        'uptime': uptime_readable,
        'cost': cost_str,
        'cost_details': cost_details  # Include cost calculation details in the response
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
