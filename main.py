from log_parser import parse_logs, generate_summary, LOG_FILE_PATH, OUTPUT_REPORT_PATH
from metrics_collector import get_system_metrics, check_alerts
from alert_manager import send_alert
from azure_uploader import upload_log_to_azure

def run_pipeline():
    print("=== AUTOMATED LOG ANALYTICS ENGINE RUNNING ===")
    
    # 1. System Metrics Check
    metrics = get_system_metrics()
    metric_alerts = check_alerts(metrics)
    if metric_alerts:
        send_alert("HIGH RESOURCE CONSUMPTION", metric_alerts)
    else:
        print("[+] System resources normal.")

    # 2. Log Parsing
    issues = parse_logs(LOG_FILE_PATH)
    generate_summary(issues)

    if issues:
        # 3. Log Errors Alert
        error_messages = [f"Line {i['line_number']}: {i['raw_log']}" for i in issues]
        send_alert("SERVER LOG ERRORS DETECTED", error_messages)
        
        # 4. Upload to Azure Blob Storage
        upload_log_to_azure(OUTPUT_REPORT_PATH)
    else:
        print("[+] No critical log errors found.")

if __name__ == "__main__":
    run_pipeline()