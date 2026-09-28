import psutil
import datetime

# Threshold limits (percentage)
CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 85.0
DISK_THRESHOLD = 90.0

def get_system_metrics():
    # Collect live usage
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    metrics = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_percent": cpu_usage,
        "memory_percent": memory_info.percent,
        "disk_percent": disk_info.percent
    }
    return metrics

def check_alerts(metrics):
    alerts = []
    
    if metrics["cpu_percent"] > CPU_THRESHOLD:
        alerts.append(f"HIGH CPU USAGE: {metrics['cpu_percent']}% (Threshold: {CPU_THRESHOLD}%)")
        
    if metrics["memory_percent"] > MEMORY_THRESHOLD:
        alerts.append(f"HIGH MEMORY USAGE: {metrics['memory_percent']}% (Threshold: {MEMORY_THRESHOLD}%)")
        
    if metrics["disk_percent"] > DISK_THRESHOLD:
        alerts.append(f"HIGH DISK USAGE: {metrics['disk_percent']}% (Threshold: {DISK_THRESHOLD}%)")
        
    return alerts

if __name__ == "__main__":
    print("[*] Gathering system metrics...")
    data = get_system_metrics()
    
    print(f"Timestamp: {data['timestamp']}")
    print(f"CPU Usage: {data['cpu_percent']}%")
    print(f"Memory Usage: {data['memory_percent']}%")
    print(f"Disk Usage: {data['disk_percent']}%")
    
    alerts = check_alerts(data)
    if alerts:
        print("\n[!] CRITICAL ALERTS TRIGGERED:")
        for alert in alerts:
            print(f" - {alert}")
    else:
        print("\n[+] All system metrics are within normal range.")