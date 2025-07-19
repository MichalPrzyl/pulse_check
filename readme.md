# Pulse check

Simple monitoring for servers and virtual machines

# Infrastructure

Simple:
- python clients sends data periodically to master 'server' via rest api
- master 'server' receives data from clients, parse it, and stores in influxDB instance
- grafana is integrated with influxDB, reads the data and (hopefully) draws nice charst

To summerize, the stack is
- python + venv
- influxDB
- grafana
