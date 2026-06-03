# Website Status Logger

A Python automation script that checks the availability of websites, records their status, and generates a timestamped log report.

## Features

* Reads website URLs from a file (`websites.txt`)
* Checks website availability using HTTP requests
* Displays HTTP status codes
* Classifies results as `UP` or `DOWN`
* Measures website response times
* Categorizes responses (Success / Redirect / Client Error / Server Error / Connection Error)
* Handles unreachable websites without crashing
* Generates a detailed log file (`status.log`)
* Exports results to CSV (`status.csv`)
* Provides a summary of healthy and unhealthy checks
* Includes a report generation timestamp and script runtime

## Project Structure

```text
Website_Status_Logger/
│
├── website_checker.py
├── websites.txt
├── status.log
├── status.csv
├── requirements.txt
└── README.md
```

## Requirements

* Python 3.10+
* requests

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Add the websites you want to monitor to `websites.txt`:

```text
https://google.com
https://github.com
https://microsoft.com
https://api.github.com
```

## Usage

Run the script:

```bash
python website_checker.py
```

After execution, files named `status.log` and `status.csv` will be generated.

## Example Output

```text
Website Status Report
=====================

Url: https://google.com
Status_code: 200
Status: UP
Healthy: True
Category: Success
Success: True
Response_time_seconds: 0.214
--------------------

====== Summary ======

Total websites checked: 4
Healthy: 4
Unhealthy: 0

Generated on: 03-06-2026 18:30:15
Script runtime: 0.45 seconds
```

## Skills Practiced

This project was built to practice:

* Python functions
* File handling
* Loops
* Dictionaries and lists
* Exception handling
* HTTP requests with the requests library
* Logging and reporting
* Basic monitoring concepts used in DevOps

## Future Improvements

* Add colored terminal output
* Send email notifications for failed websites
* Read configuration from a JSON file
* Schedule execution with Cron or Task Scheduler
* Containerize the application with Docker

## Author

Built as part of a DevOps learning journey focused on automation, monitoring, and Python scripting.
