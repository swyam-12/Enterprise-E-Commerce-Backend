from fastapi import FastAPI
from src.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Enterprise App Running 🚀"}