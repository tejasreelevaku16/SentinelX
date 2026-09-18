from fastapi import FastAPI

app = FastAPI(title="SentinelX")

@app.get("/")
def home():
    return {
        "project": "SentinelX",
        "status": "running",
        "message": "Cybersecurity platform is online"
    }
