import requests
import csv
import os
import time

# API endpoint
url = "http://api.open-notify.org/iss-now.json"

# CSV file path
csv_file = "iss_location.csv"

# Check if file exists to decide if header is needed
file_exists = os.path.isfile(csv_file)

# Open CSV file once in append mode
with open(csv_file, mode="a", newline="") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(["timestamp", "longitude", "latitude"])  # header

    while True:
        try:
            # Request ISS position
            response = requests.get(url)
            data = response.json()

            # Extract fields
            timestamp = data['timestamp']
            longitude = data['iss_position']['longitude']
            latitude = data['iss_position']['latitude']

            # Write to CSV
            writer.writerow([timestamp, longitude, latitude])
            file.flush()  # ensure data is written immediately

            print(f"Saved: {timestamp}, {longitude}, {latitude}")

        except Exception as e:
            print(f"Error: {e}")

        # Wait 10 seconds before next request
        time.sleep(10)
