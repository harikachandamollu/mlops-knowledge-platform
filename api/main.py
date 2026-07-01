from fastapi import FastAPI

app = FastAPI(
    title = "MLOps Knowledge Platform",
    description = "RAG system for MLOps + Data Engineering knowledge"
)

@app.get("/")
def home():
    return {"message": "MLOps Knowledge Platform is running"}