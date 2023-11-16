from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from helper import imdsv2
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    # Encode response into JSON
    response = jsonable_encoder({
        "instance-id": imdsv2.getInstanceID(), # Get instance ID from IMDSv2
        "local-hostname": imdsv2.getInstanceHostname(), # Get instance local hostname from IMDSv2
    })
    # Send the response
    return JSONResponse(content=response)

# Debug only
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)