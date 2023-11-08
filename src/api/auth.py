from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from src.schemas.token import TokenPayloadSchema, TokenSchema
from src.schemas.user import UserCreateSchema, UserResponseSchema
from src.service import AuthService
from src.token.token import Token


router = APIRouter(
    prefix="/api/auth",
    tags=["auth"]
)


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponseSchema
)
async def register(schema: UserCreateSchema, service: AuthService = Depends()):
    user = await service.create_user(schema)
    return user


@router.post("/token", response_model=TokenSchema)
async def login(
    schema: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends()
):
    token = await service.login(schema.username, schema.password)
    return token


@router.post("/introspect", response_model=TokenPayloadSchema)
async def introspect_token(user_info: TokenPayloadSchema = Depends(Token.verify_token)):
    return user_info
