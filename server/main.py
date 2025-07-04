from fastapi import FastAPI
from routes.auth import router
app = FastAPI()

app.include_router(router,prefix="/api")

@app.get("/")
def intro():
    return "Hello World"

