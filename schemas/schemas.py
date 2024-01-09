from pydantic import BaseModel, ConfigDict
from fastapi_users import schemas as fastapi_users_schemas


# Inherit from when creating Pydantic Models
class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    # This model_config lets pydantic validate a databse model


class PostRead(BaseSchema):
    id: int
    name: str


class UserRead(fastapi_users_schemas.BaseUser[int], BaseSchema):
    firstname: str
    email: str
    posts: list[PostRead]  # uncommenting this makes the route work


class UserCreate(fastapi_users_schemas.BaseUserCreate, BaseSchema):
    firstname: str
    pass
