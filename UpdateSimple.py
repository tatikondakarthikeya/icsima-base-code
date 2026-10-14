import os
import requests

url = os.environ.get("GOOGLE_APPS_SCRIPT_URL", "")
if not url:
    raise SystemExit("Set GOOGLE_APPS_SCRIPT_URL to your authorized Apps Script endpoint.")

try:
    response = requests.get(url, params={"RunStatus": 12}, timeout=10)
    print("Status:", response.status_code)
    print("Response:", response.text)
except requests.RequestException as exc:
    print(f"Request failed: {exc}")
