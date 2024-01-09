from sqlalchemy import ForeignKey
from .base_model import BaseModel_DB
from sqlalchemy.orm import Mapped, mapped_column


class Post_DB(BaseModel_DB):
    __tablename__ = "post_table"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
