from fastapi import FastAPI

app = FastAPI(
    title="Medicare API",
    description="Health Management Backend System",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Medicare API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}