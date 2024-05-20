from fastapi import FastAPI

from services.pooled_db_service import get_db, engine, Base
from services.db_service import dis_connect_all, connect_all
from routes import router as api_routers
from logger import log_config

app = FastAPI()
app.include_router(api_routers)


@app.on_event("startup")
async def app_startup():
    log_config.logger.info("app startup ...")
    connect_all()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def app_shutdown():
    log_config.logger.info("app shutdown ...")
    dis_connect_all()
    await engine.dispose()
