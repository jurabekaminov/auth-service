from fastapi import FastAPI

from src.api import router


app = FastAPI(
    title="Auth service",
    description="Digital twin auth microservice.",
    version="0.0.1"
)

app.include_router(router)
