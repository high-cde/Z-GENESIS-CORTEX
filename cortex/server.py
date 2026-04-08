from fastapi import FastAPI
from router import router

app = FastAPI(title="Z‑CORTEX")
app.include_router(router)

@app.get("/")
def root():
    return {"status": "Z‑CORTEX online"}
