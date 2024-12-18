import requests
import json
import time

# Define the file path and the remote server URL
input_file = "gps.txt"
url = "http://127.0.0.1:9090/api/v1/DHLqFmaKUDn1Q1XTdN6Q/telemetry"

# Function to send GPS data to the server
def send_data(file_path, server_url):
    try:
        with open(file_path, "r") as f:
            for line in f:
                try:
                    # Parse each line as a JSON object
                    data = json.loads(line.strip())

                    # Prepare the payload for the server
                    payload = {
                        "ts": data["ts"],
                        "latitude": data["latitude"],
                        "longitude": data["longitude"]
                    }

                    # Send the data to the server
                    headers = {"Content-Type": "application/json"}
                    resp = requests.post(server_url, headers=headers, data=json.dumps(payload))

                    # Print the response from the server
                    if resp.status_code == 200:
                        print("Data sent successfully:", payload)
                    else:
                        print(f"Failed to send data: {resp.status_code}, {resp.text}")
                except json.JSONDecodeError:
                    print("Invalid JSON format in line:", line)
                except Exception as e:
                    print(f"Error sending data: {e}")

        print("Finished sending all data.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except KeyboardInterrupt:
        print("\nStopping data transmission. Goodbye!")

# Start reading and sending data
if __name__ == "__main__":
    send_data(input_file, url)
