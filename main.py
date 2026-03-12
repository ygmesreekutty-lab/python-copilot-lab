import uuid
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# This is the existing endpoint Mr. John mentioned
@app.get("/")
async def read_root():
    return {"message": "Welcome to the ABC Project Token - Rajasree", "token": str(uuid.uuid4())}

# Step 1: Mark, you will add the Pydantic model below this line using Copilot
