<div align="center">
   <h1> Server-Insights</h1>
    <!-- <img src="" alt="Profile Image" style="border-radius: 50%; width: 300px; height: 300px; object-fit: cover;"> -->
        <p>This lightweight Flask-based web application provides real-time monitoring of AWS EC2 instances or any server resources including CPU, memory, and storage utilization. It also displays the uptime and calculates the ongoing costs based on the EC2 instance type and usage.</p>
</div>

## ⭐ Features

- **Real-Time Resource Utilization:** Monitor CPU, memory, and storage usage in real-time.
- **System Uptime:** View system uptime in a human-readable format (days, hours, minutes).
- **Cost Calculation:** Track the cost associated with the EC2 instance up to the current time based on predefined hourly rates.

## 🔧 How to Install

### 🐳 Docker

```bash
docker run -d --restart=always -p 8080:8080 --name resources osamayusuf/resource-insight:v1
```

Server-Insights is now running on [http://localhost:8080](http://localhost:8080).

### 💪🏻 Non-Docker

1. Clone the repository or download the source code.
2. Navigate to the app directory and install the required packages:

   ```bash
   pip install flask psutil
   ```

3. Run the Flask app:

   ```bash
   python app.py
   ```

Server-Insights is now running on [http://localhost:8080](http://localhost:8080).

## Usage

- Open a web browser and navigate to `http://localhost:8080` to view the dashboard.
- The `/get_resource_usage` endpoint can be accessed directly to fetch JSON data regarding the resource usage and cost.

### API Endpoints

- `GET /` - The main dashboard displaying resource metrics in a graphical interface.
- `GET /get_resource_usage` - Returns JSON data containing CPU, memory, storage usage, uptime, and cost details.

## How It Works

- **Resource Usage:** Utilizes the `psutil` library to fetch real-time resource metrics.
- **Uptime:** Reads from `/proc/uptime` to calculate the system uptime.
- **Cost Calculation:** Fetches the instance type from EC2 metadata and calculates the cost based on uptime and predefined hourly rates for various EC2 instance types.

## Configuring Hourly Rates

To update or modify the hourly rates for EC2 instances, adjust the `hourly_rates` dictionary in the `get_resource_usage` function with the desired rates corresponding to different EC2 instance types.

## Contributing

Contributions are welcome, and any help that can improve the project is appreciated. Here’s how you can contribute:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -am 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

osama9mohamed5@gmail.com
[GitHub Repo](https://github.com/osama-yusuf/Server-Insights)
