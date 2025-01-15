from fastapi import FastAPI
from app.routers import user, task

app = FastAPI(title="Task Manager", description="A simple task manager app")

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(task.router, prefix="/tasks", tags=["Tasks"])

@app.get("/", tags=["Welcome"])
def welcome():
    return {"message": "Welcome to the Task Manager!"}






