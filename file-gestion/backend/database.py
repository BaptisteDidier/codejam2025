import asyncpg
import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from fastapi import FastAPI

load_dotenv()
db_pool: asyncpg.pool.Pool | None = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global db_pool
    db_pool = await asyncpg.create_pool(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME"),
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 5432)),
    )
    yield
    await db_pool.close()
