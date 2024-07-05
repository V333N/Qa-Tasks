import psutil
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s:%(message)s')

# Define thresholds
CPU_THRESHOLD = 80.0  # in percentage
MEMORY_THRESHOLD = 80.0  # in percentage
DISK_THRESHOLD = 80.0  # in percentage
PROCESS_COUNT_THRESHOLD = 200  # number of processes

def log_alert(message):
    print(message)
    logging.info(message)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"High CPU usage detected: {cpu_usage}%")

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f"High Memory usage detected: {memory_usage}%")

def check_disk_space():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        log_alert(f"Low Disk Space detected: {disk_usage}% used")

def check_running_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_COUNT_THRESHOLD:
        log_alert(f"High number of running processes detected: {process_count}")

def monitor_system_health():
    log_alert("Starting system health monitoring...")
    check_cpu_usage()
    check_memory_usage()
    check_disk_space()
    check_running_processes()
    log_alert("System health monitoring completed.")

if __name__ == "__main__":
    monitor_system_health()
