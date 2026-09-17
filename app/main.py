from fastapi import FastAPI

app = FastAPI(title="LexiGuard AI", version="0.1.0")

@app.get("/healthz")
async def health_check():
    return {"status": "ok", "service": "LexiGuard AI"}
