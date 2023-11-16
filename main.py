from fastapi import FastAPI
from helper import imdsv2
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {
        "instance-id": imdsv2.getInstanceID(),
        "local-hostname": imdsv2.getInstanceHostname(),
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)