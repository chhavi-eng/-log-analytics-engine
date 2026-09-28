import os
from datetime import datetime

LOG_FILE_PATH = "sample_server.log"
OUTPUT_REPORT_PATH = "parsed_errors.log"

TARGET_LEVELS = ["ERROR", "CRITICAL"]

def parse_logs(file_path):
    if not os.path.exists(file_path):
        print(f"[!] Log file not found at: {file_path}")
        return []

    identified_issues = []
    with open(file_path, "r") as file:
        for line_num, line in enumerate(file, start=1):
            line = line.strip()
            for level in TARGET_LEVELS:
                if f" {level} " in line:
                    identified_issues.append({
                        "line_number": line_num,
                        "level": level,
                        "raw_log": line
                    })
                    break
    return identified_issues

def generate_summary(issues):
    total_issues = len(issues)
    print("\n" + "="*45)
    print(f" LOG ANALYSIS SUMMARY - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*45)
    print(f"Total Critical/Error issues detected: {total_issues}\n")

    with open(OUTPUT_REPORT_PATH, "w") as out:
        for issue in issues:
            display_str = f"[Line {issue['line_number']}] [{issue['level']}] {issue['raw_log']}"
            print(display_str)
            out.write(display_str + "\n")
            
    print("="*45)
    print(f"[*] Filtered logs saved to: {OUTPUT_REPORT_PATH}")