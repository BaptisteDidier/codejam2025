from fastapi import APIRouter, UploadFile, File, HTTPException
from database import db_pool

MAX_SIZE = 3 * 1024 * 1024
router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    size = len(content)

    if size > MAX_SIZE:
        raise HTTPException(status_code=400, detail="File too large")

    query = """
        INSERT INTO uploads (filename, content, mimetype)
        VALUES ($1, $2, $3)
        RETURNING id, uploaded_at;
    """

    async with db_pool.acquire() as c:
        row = await c.fetchrow(query, file.filename, content, file.content_type)

    return {
        "id": row["id"],
        "filename": row["filename"],
        "uploaded_at": row["uploaded_at"].isoformat()
    }
