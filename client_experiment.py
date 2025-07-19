import psutil
import json
from datetime import datetime

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

def main():
    metrics = get_system_metrics()
    print(json.dumps(metrics, indent=2))

if __name__ == "__main__":
    main()
