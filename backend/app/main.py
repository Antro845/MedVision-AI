from fastapi import FastAPI

app = FastAPI(
    title="MedVision AI",
    version="1.0.0",
    description="Medical Imaging Analysis Platform"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to MedVision AI",
        "status": "Backend Running Successfully"
    }