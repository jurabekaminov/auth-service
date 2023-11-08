from fastapi import FastAPI

from src.api.auth import router as auth_router
from src.api.users import router as users_router


app = FastAPI(
    title="Auth service",
    description="Digital twin auth microservice.",
    version="0.0.1"
)

app.include_router(auth_router)
app.include_router(users_router)
