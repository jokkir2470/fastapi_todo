from fastapi import FastAPI
from app.api.routes_todo import router as task_router
from app.api.routes_user import router as user_router

app = FastAPI(title= "ToDo API")
app.include_router(task_router, prefix="/tasks", tags= ["tasks"])
app.include_router(user_router, prefix="/users", tags= ["users"])
@app.get("/")
def root():
    return {"status":"ok", "api": "ToDo", "version": 1}