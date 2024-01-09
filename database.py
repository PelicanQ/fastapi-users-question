from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from db_models import *


# SQLite database will be a single file at project root
SQLALCHEMY_DATABASE_URL_ASYNC = "sqlite+aiosqlite:///./database.sqlite"


async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL_ASYNC, echo=True)

async_sessionmaker = async_sessionmaker(async_engine, expire_on_commit=False)


async def create_db_and_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(BaseModel_DB.metadata.create_all)


# A route accesses DB by Depends()'ing on this:
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_sessionmaker() as session:
        yield session
