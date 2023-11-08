from pydantic import BaseModel, Field

from src.utils.roles import RoleEnum


class UserUpdateSchema(BaseModel):
    email: str = Field(max_length=128)
    text_password: str = Field(max_length=64)


class UserCreateSchema(UserUpdateSchema):
    role: RoleEnum


class UserResponseSchema(BaseModel):
    id: int
    email: str = Field(max_length=128)
    role: RoleEnum
    created_by: int | None = None
