import time
from monitoring_dashboard.metrics import get_cpu_usage, get_memory_usage, get_disk_usage

def display_metrics():
    try:
        while True:
            cpu = get_cpu_usage()
            memory = get_memory_usage()
            disk = get_disk_usage()
            print("\033c", end="")  # Clear terminal
            print(f"🖥️  CPU Usage:    {cpu}%")
            print(f"🧠 Memory Usage: {memory}%")
            print(f"💽 Disk Usage:   {disk}%")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
