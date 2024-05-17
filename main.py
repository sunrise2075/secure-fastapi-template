from fastapi import FastAPI

from routes import auth, task
from services.database_service import dis_connect_all, connect_all

app = FastAPI()
app.include_router(auth.router)
app.include_router(task.router)


@app.on_event("startup")
async def app_startup():
    connect_all()


@app.on_event("shutdown")
async def app_shutdown():
    dis_connect_all()
