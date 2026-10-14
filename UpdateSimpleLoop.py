import os
import time
import requests

url = os.environ.get("GOOGLE_APPS_SCRIPT_URL", "")
if not url:
    raise SystemExit("Set GOOGLE_APPS_SCRIPT_URL to your authorized Apps Script endpoint.")

while True:
    try:
        response = requests.get(url, params={"RunStatus": 0}, timeout=10)
        print("Status:", response.status_code)
        print("Response:", response.text)
    except requests.RequestException as exc:
        print(f"Request failed: {exc}")
    time.sleep(10)
