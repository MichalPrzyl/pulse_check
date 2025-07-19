from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/api/data")
async def receive_metrics(request: Request):
    body = await request.json()
    print(f"Received from {body['hostname']}: CPU {body['cpu_percent']}%, RAM {body['memory']['percent']}%")
    return {"status": "ok"}
