# Automated Log Analytics Engine

A lightweight Python and Bash automation pipeline designed to monitor server runtime metrics, extract and parse system logs for critical anomalies, push alerts, and archive structured reports to Azure Blob Storage.

## Features
- **Runtime Metrics Monitoring**: Live tracking of CPU, RAM, and Disk utilization using `psutil`.
- **Log Parsing Engine**: Automatic extraction of `ERROR` and `CRITICAL` entries from server logs.
- **Alert System**: Immediate console alert triggers for infrastructure breaches.
- **Cloud Archival**: Seamless log archiving using Azure Blob Storage SDK.
- **Automation Ready**: Linux shell runner script for cron job scheduling.

## Tech Stack
- **Language**: Python 3.x, Bash
- **Cloud**: Azure VMs, Azure Blob Storage
- **Libraries**: `azure-storage-blob`, `psutil`, `python-dotenv`

## Project Architecture
```text
log-analytics-engine/
│
├── alert_manager.py       # Alert formatting and triggers
├── azure_uploader.py      # Azure Blob Storage SDK integration
├── log_parser.py          # Log filtering and report generation
├── metrics_collector.py   # CPU, RAM, and Disk health monitor
├── main.py                # Pipeline entry point
├── sample_server.log      # Raw log inputs
├── parsed_errors.log      # Processed error reports
├── run_engine.sh          # Automation shell script
└── requirements.txt       # Dependencies
