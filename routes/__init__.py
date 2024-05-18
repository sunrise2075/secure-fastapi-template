from fastapi import APIRouter
from routes import auth, task


router = APIRouter()
router.include_router(auth.router)
router.include_router(task.router)