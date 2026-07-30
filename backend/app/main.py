from fastapi import FastAPI

app = FastAPI(
    title="Ticket Platform v2",
    version="0.1.0"
)

@app.get("/")
def health():
    return {
        "status": "running",
        "service": "ticket-platform-backend"
    }
