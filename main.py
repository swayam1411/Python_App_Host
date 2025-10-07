import os
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_hello():
    return {"Hey"}

@app.get("/hello-abhi")
def read_hello():
    return {"Hey, Hello Abhi"}

@app.get("/hello")
def read_hello():
    return {"message": "Hello from FastAPI on Railway!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)