import psutil
cpu_percent = psutil.cpu_percent()
virtual_memory = psutil.virtual_memory()
dict(psutil.virtual_memory()._asdict())
x = psutil.virtual_memory().percent
y = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total

print(f"x: {x}")
print(f"y: {y}")
