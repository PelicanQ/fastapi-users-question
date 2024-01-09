from typing import TYPE_CHECKING

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, relationship, mapped_column
from .base_model import BaseModel_DB
from sqlalchemy.orm import MappedAsDataclass

if TYPE_CHECKING:
    from .post_model import Post_DB


class Mixin(MappedAsDataclass, SQLAlchemyBaseUserTable[int]):
    pass


class User_DB(BaseModel_DB, Mixin):
    __tablename__ = "user_table"
    id: Mapped[int] = mapped_column(primary_key=True, init=False)  # type: ignore . It's fine

    firstname: Mapped[str] = mapped_column()

    posts: Mapped[list["Post_DB"]] = relationship(init=False)
