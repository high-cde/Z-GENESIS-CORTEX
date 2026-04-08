from fastapi import APIRouter
from controllers import add, query, zaaak, rooms

router = APIRouter()

router.include_router(add.router)
router.include_router(query.router)
router.include_router(zaaak.router)
router.include_router(rooms.router)
