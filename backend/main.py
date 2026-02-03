from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="SmartOps Data Platform")

Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {"status": "ok"}
