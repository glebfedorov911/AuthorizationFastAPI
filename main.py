from fastapi import FastAPI

from app.v1.auth.views import router as auth_router

import uvicorn


app = FastAPI()
app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)