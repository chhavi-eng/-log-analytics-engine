import datetime

def send_alert(alert_title, details_list):
    """
    Console alert generate karta hai.
    (Isko Slack/Discord webhook ya Email se bhi connect kiya ja sakta hai)
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("\n" + "#"*50)
    print(f" [ALERT TRIGGERED] - {timestamp}")
    print(f" TYPE: {alert_title}")
    print("#"*50)
    
    for item in details_list:
        print(f" -> {item}")
        
    print("#"*50 + "\n")