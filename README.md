# Website Status Logger

[![Python Check](https://github.com/Zakzi-Devops/website-status-logger/actions/workflows/python-check.yml/badge.svg)](https://github.com/Zakzi-Devops/website-status-logger/actions/workflows/python-check.yml)

A Python-based monitoring tool that checks website and API availability, measures response times, classifies HTTP responses, handles connection errors, and generates timestamped log and CSV reports.

---

# Version

**Current Version:** v2.0

### What's New in v2.0

* Dockerized application
* Added Dockerfile
* Added .dockerignore
* Added volume support for report persistence
* Reports can be generated directly from a Docker container

---

# Features

* Reads website URLs from a file (`websites.txt`)
* Checks website and API availability using HTTP requests
* Displays HTTP status codes
* Classifies results as UP or DOWN
* Measures website response times
* Categorizes responses:

  * Success
  * Redirect
  * Client Error
  * Server Error
  * Connection Error
  * Timeout Error
  * SSL Error
* Handles unreachable websites without crashing
* Generates a detailed log report (`status.log`)
* Exports results to CSV (`status.csv`)
* Provides a summary of healthy and unhealthy checks
* Includes report generation timestamp
* Includes script runtime measurement
* Dockerized for portable and consistent execution
* Supports volume mounts to save reports outside the container

---

# Project Structure

```text
Website_Status_Logger/
│
├── website_checker.py
├── websites.txt
├── output/
│   ├── status.log
│   └── status.csv
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Requirements

## Local Execution

* Python 3.10+
* requests

Install dependencies:

```bash
pip install -r requirements.txt
```

## Docker Execution

* Docker Desktop
* Docker Engine

---

# Configuration

Add the websites or APIs you want to monitor to `websites.txt`.

Example:

```text
https://google.com
https://github.com
https://microsoft.com
https://api.github.com
https://jsonplaceholder.typicode.com/posts
```

---

# Usage

## Local Python Execution

Run the script:

```bash
python website_checker.py
```

After execution, reports will be generated in:

```text
output/status.log
output/status.csv
```

---

# Docker Usage

## Build the Docker Image

```bash
docker build -t website-status-logger .
```

## Create Output Directory

```bash
mkdir output
```

## Run the Container

### PowerShell (Recommended)

```powershell
docker run --rm -v "${PWD}/output:/app/output" website-status-logger
```

### Git Bash

If path conversion issues occur in Git Bash, use an absolute Windows path:

```bash
docker run --rm -v "C:/Users/your-user/Devops/Website_Status_Logger/output:/app/output" website-status-logger
```

After execution, reports will be available in:

```text
output/status.log
output/status.csv
```

---

# Dockerfile Overview

The Dockerfile:

* Uses `python:3.12-slim` as the base image
* Sets `/app` as the working directory
* Installs Python dependencies from `requirements.txt`
* Copies project files into the container
* Creates an `/app/output` directory for generated reports
* Runs `website_checker.py` when the container starts

---

# Example Log Output

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

---

# Example CSV Output

```csv
Url,Status_code,Status,Healthy,Category,Success,Response_time_seconds,Error
https://google.com,200,UP,True,Success,True,0.214,
https://github.com,200,UP,True,Success,True,0.320,
https://microsoft.com,200,UP,True,Success,True,0.487,
https://api.github.com,200,UP,True,Success,True,0.158,
```

**Note:** The `Error` column is included in the CSV export and is populated only when a request fails or raises an exception.

---

# Ignored Files

This project uses both `.gitignore` and `.dockerignore`.

## .gitignore

The `.gitignore` file excludes files from Git version control, such as:

* Generated `.log` and `.csv` reports
* Python cache files
* Virtual environments
* Environment files
* VS Code settings

## .dockerignore

The `.dockerignore` file excludes unnecessary files from the Docker build context, such as:

* `.git`
* Python cache files
* Generated `.log` and `.csv` reports
* Virtual environments
* Environment files
* VS Code settings

This keeps the Git repository clean and helps keep Docker images smaller and builds faster.

---

# Skills Practiced

This project was built to practice:

* Python functions
* File handling
* Loops
* Dictionaries and lists
* Exception handling
* HTTP requests with the requests library
* Logging and reporting
* CSV generation
* Docker fundamentals
* Docker images and containers
* Docker volume mounts
* Basic monitoring concepts used in DevOps

---

# Future Improvements

* Add GitHub Actions CI/CD pipeline
* Publish Docker image to Docker Hub
* Deploy the application to Azure
* Add email or Teams notifications
* Add JSON output format
* Add colored terminal output
* Read configuration from a JSON or YAML file
* Schedule execution with Cron or Windows Task Scheduler

---

# Version History

## v2.0

* Dockerized application
* Added Dockerfile
* Added .dockerignore
* Added volume support for report persistence

## v1.0

* Website and API monitoring
* CSV report generation
* Log report generation
* Response time measurements
* Error handling and categorization

---

# Author

Built as part of a DevOps learning journey focused on:

* Linux
* Python Automation
* Git & GitHub
* Docker
* Monitoring
* CI/CD
* Cloud & DevOps Engineering
