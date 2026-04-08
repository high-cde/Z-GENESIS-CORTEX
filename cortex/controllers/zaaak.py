from fastapi import APIRouter

router = APIRouter(prefix="/zaaak", tags=["zaaak"])

@router.post("/encode")
def encode(payload: dict):
    return {"encoded": "TODO"}

@router.post("/decode")
def decode(payload: dict):
    return {"decoded": "TODO"}
