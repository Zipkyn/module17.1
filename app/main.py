from fastapi import FastAPI
from app.backend.db import Base, engine
from app.routers.user_router import router as user_router
from app.routers.task_router import router as task_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
app.include_router(task_router)

@app.get("/", tags=["Root"])
def welcome():
    return {"message": "Welcome to the Task Manager API!"}








