from fastapi import APIRouter

router = APIRouter(prefix="/add", tags=["add"])

@router.post("/")
def add_item(payload: dict):
    return {"status": "ok", "received": payload}
