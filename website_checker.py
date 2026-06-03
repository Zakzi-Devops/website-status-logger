import requests
import csv
import time
from datetime import datetime


website_file = "websites.txt"
log_file = "status.log"
csv_file = "status.csv"
TIMEOUT = 10

def read_websites(file_path):
    with open(file_path, "r") as website_read:
        return website_read.readlines()


def classify_status(status_code):
    if 200 <= status_code < 300:
        return "Success"
    elif 300 <= status_code < 400:
        return "Redirect"
    elif 400 <= status_code < 500:
        return "Client Error"
    elif 500 <= status_code < 600:
        return "Server Error"
    else:
        return "Connection Error"

start_time = time.time()

def check_website(url):
    try:
        
        url = url.strip()
        response = requests.get(url, timeout=TIMEOUT)
        healthy = 200 <= response.status_code < 400
        category = classify_status(response.status_code)
        status = "UP" if healthy else "DOWN"
        return {
            "Url": url,
            "Status_code": response.status_code,
            "Status": status,
            "Healthy": healthy,
            "Category": category,
            "Success": response.ok,
            "Response_time_seconds": response.elapsed.total_seconds()
        }
        
    except requests.Timeout as excep:
        category = "Timeout Error"
        return {
            "Url": url,
            "Status_code": None,
            "Status": "DOWN",
            "Healthy": False,
            "Category": category,
            "Success": False,
            "Error": str(excep),
        }
    
    except requests.exceptions.SSLError as excep:
        category = "SSL Error"
        return {
            "Url": url,
            "Status_code": None,
            "Status": "DOWN",
            "Healthy": False,
            "Category": category,
            "Success": False,
            "Error": str(excep),
        }

    except requests.ConnectionError as excep:
        category = "Connection Error"
        return {
            "Url": url,
            "Status_code": None,
            "Status": "DOWN",
            "Healthy": False,
            "Category": category,
            "Success": False,
            "Error": str(excep),
        }
    
    except requests.RequestException as excep:
        category = "Request Error"
        return {
            "Url": url,
            "Status_code": None,
            "Status": "DOWN",
            "Healthy": False,
            "Category": category,
            "Success": False,
            "Error": str(excep),
        }
    
websites_list = read_websites(website_file)

website_results = []

for website in websites_list:
    result = check_website(website)
    website_results.append(result)


def write_log(results, script_runtime):
    with open(log_file, 'w', encoding="utf-8") as logs:
        logs.write("Website Status Report\n")
        logs.write("=====================\n \n")

        successful = 0
        failed = 0

        for result in results:
            for key, value in result.items():
                logs.write(f"{key}: {value}\n")
            logs.write(f"--------------------\n \n")
        
            if result["Healthy"] == True:
                successful += 1
            else:
                failed += 1
        logs.write("====== Summary ======\n \n")
        logs.write(f"Total websites checked: {len(results)}\n")
        logs.write(f"Healthy: {successful}\n")
        logs.write(f"Unhealthy: {failed}\n \n")
        logs.write(f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n \n")
        logs.write(f"Script runtime: {script_runtime:.2f} seconds\n")

def write_csv(results):
    with open(csv_file, 'w', newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Url", "Status_code", "Status", "Healthy", "Category", "Success", "Response_time_seconds", "Error"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for result in results:
            writer.writerow(result)

write_csv(website_results)

end_time = time.time()
script_runtime = end_time - start_time

write_log(website_results, script_runtime)

print("Reports saved to status.log and status.csv")
print(f"Script completed in {script_runtime:.2f} seconds")