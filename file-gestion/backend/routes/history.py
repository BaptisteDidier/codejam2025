from fastapi import APIRouter
from fastapi.responses import JSONResponse
from database import db_pool

router = APIRouter()

@router.get("/history")
async def get_upload_history(limit: int = 10, offset: int = 0):
    query = """
        SELECT id, filename, size, mimetype, uploaded_at
        FROM uploaded_files
        ORDER BY uploaded_at DESC
        LIMIT $1 OFFSET $2
    """
    async with db_pool.acquire() as conn:
        rows = await conn.fetch(query, limit, offset)

    history = [dict(row) for row in rows]
    return JSONResponse({"history": history})