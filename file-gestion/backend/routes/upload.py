from fastapi import APIRouter, UploadFile, File, HTTPException
from database import db_pool

MAX_SIZE = 3 * 1024 *1024
router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    size = len(content)

    if size > MAX_SIZE:
        raise HTTPException(status_code=400, detail="File too large")

    query = """
        INSERT INTO files (filename, content)
        VALUES ($1, $2)
        RETURNING id;
    """

    async with db_pool.acquire() as c:
        file_id = await c.fetchval(query, file.filename, content)

    return {"id": file_id}
