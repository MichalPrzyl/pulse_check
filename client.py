import psutil
import json
import requests
from datetime import datetime

MASTER_URL = "http://localhost:8000/api/data"
HOSTNAME = "server-01"

def get_system_metrics():
    cpu = psutil.cpu_percent(interval=1.0)
    memory = psutil.virtual_memory()._asdict()

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "hostname": HOSTNAME,
        "cpu_percent": cpu,
        "memory": {
            "total": memory["total"],
            "available": memory["available"],
            "used": memory["used"],
            "percent": memory["percent"]
        }
    }

def send_metrics(data, url):
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Send error: {e}")

def main():
    metrics = get_system_metrics()
    send_metrics(metrics, MASTER_URL)

if __name__ == "__main__":
    main()

