import os
import time
import requests

ISS_URL = "http://api.open-notify.org/iss-now.json"
APPS_SCRIPT_URL = os.environ.get("GOOGLE_APPS_SCRIPT_URL", "")
if not APPS_SCRIPT_URL:
    raise SystemExit("Set GOOGLE_APPS_SCRIPT_URL to your authorized Apps Script endpoint.")

while True:
    try:
        response = requests.get(ISS_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        timestamp = data["timestamp"]
        longitude = data["iss_position"]["longitude"]
        latitude = data["iss_position"]["latitude"]

        sent = requests.get(
            APPS_SCRIPT_URL,
            params={"Longitude": longitude, "Latitude": latitude},
            timeout=10,
        )
        print("Status:", sent.status_code)
        print("Response:", sent.text)
        print(f"Sent ISS position: {timestamp}, {longitude}, {latitude}")
    except (requests.RequestException, KeyError, ValueError) as exc:
        print(f"Error: {exc}")
    time.sleep(10)
