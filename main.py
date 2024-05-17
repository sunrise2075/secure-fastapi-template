from fastapi import FastAPI

from routes import auth
from routes import task

app = FastAPI()

app.include_router(auth.router)
app.include_router(task.router)

