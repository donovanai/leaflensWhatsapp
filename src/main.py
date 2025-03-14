import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "LeafLens API is running!"}

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", 8000))  # Use Railway's assigned port
    uvicorn.run(app, host="0.0.0.0", port=PORT)
