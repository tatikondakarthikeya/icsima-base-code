import os
import time
import requests
import psutil

url = os.environ.get("GOOGLE_APPS_SCRIPT_URL", "")
if not url:
    raise SystemExit("Set GOOGLE_APPS_SCRIPT_URL to your authorized Apps Script endpoint.")

TARGET = "AcquireData.py"

while True:
    found = False
    for proc in psutil.process_iter(["pid", "name", "cmdline"]):
        try:
            if proc.info["cmdline"] and any(TARGET in part for part in proc.info["cmdline"]):
                print(f"{TARGET} is running with PID {proc.info['pid']}")
                found = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    try:
        response = requests.get(url, params={"RunStatus": int(found)}, timeout=10)
        print("Status:", response.status_code)
        print("Response:", response.text)
    except requests.RequestException as exc:
        print(f"Request failed: {exc}")
    time.sleep(10)
