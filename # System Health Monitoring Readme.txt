# System Health Monitoring Script

## Overview
This Python script monitors the health of a Linux system by checking CPU usage, memory usage, disk space, and running processes. If any of these metrics exceed predefined thresholds (e.g., CPU usage > 80%), the script sends an alert to the console and logs the alert to a log file.

## Prerequisites
- Python 3.x
- `psutil` library

## Setup

### Step 1: Install Python
Ensure that Python is installed on your system. You can download Python from [python.org](https://www.python.org/).

### Step 2: Install `psutil`
Install the `psutil` library using `pip`. Open a terminal and run:
```bash
pip install psutil
Step 3: Download the Script
Download the system_health_monitor.py script and save it to your desired directory.

Configuration
The script includes predefined thresholds for monitoring. You can adjust these thresholds as needed:

# Define thresholds
CPU_TH
RESHOLD = 80.0  # in percentage
MEMORY_THRESHOLD = 80.0  # in percentage
DISK_THRESHOLD = 80.0  # in percentage
PROCESS_COUNT_THRESHOLD = 200  # number of processes
Execution
Step 1: Navigate to the Script Directory
Open a terminal and navigate to the directory where you saved the system_health_monitor.py script. For example:

cd /path/to/your/script


Step 2: Run the Script
Execute the script by running:

python system_health_monitor.py


Expected Output
The script will check the system's CPU usage, memory usage, disk space, and number of running processes. If any metrics exceed the defined thresholds, the script will log alerts to the console and the system_health.log file.

Example Console Output:

Starting system health monitoring...
High CPU usage detected: 85.0%
High Memory usage detected: 82.5%
Low Disk Space detected: 81.0% used
High number of running processes detected: 205
System health monitoring completed.


Example Log File Output (system_health.log)

INFO:Starting system health monitoring...
INFO:High CPU usage detected: 85.0%
INFO:High Memory usage detected: 82.5%
INFO:Low Disk Space detected: 81.0% used
INFO:High number of running processes detected: 205
INFO:System health monitoring completed.


Customization
You can modify the script to add additional checks or customize the alerting mechanism. The script is designed to be modular and easy to extend.

License
This script is provided under the MIT License. You are free to use, modify, and distribute it as needed.

Contact
For questions or feedback, please contact Prajjwal Sharma at Prajjwalsharma.vyas2016@gmail.com.


This README file provides a comprehensive guide for setting up, configuring, and running the System Health Monitoring script. Adjust the placeholders (e.g., your name, email) as needed.





