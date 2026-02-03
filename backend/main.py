from fastapi import FastAPI

app = FastAPI(title="SmartOps Test Project")

@app.get("/")
def healthCheck():
    return {"status":"ok"}