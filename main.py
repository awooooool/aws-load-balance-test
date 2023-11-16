from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from helper import imdsv2
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    response = jsonable_encoder({
        "instance-id": imdsv2.getInstanceID(),
        "local-hostname": imdsv2.getInstanceHostname(),
    })
    return JSONResponse(content=response)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)