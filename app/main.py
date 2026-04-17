from fastapi import FastAPI
from app.api.routes import key, protected

app = FastAPI(title="API Key Service")

app.include_router(key.router)
app.include_router(protected.router)

@app.get("/")
def root():
    return {"message": "Service is running"}