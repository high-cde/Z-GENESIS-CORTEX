from fastapi import APIRouter

router = APIRouter(prefix="/query", tags=["query"])

@router.post("/")
def query_item(payload: dict):
    return {"status": "ok", "results": []}
