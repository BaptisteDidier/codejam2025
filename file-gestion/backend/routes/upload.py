from fastapi import APIRouter, UploadFile, File, HTTPException
from database import db_pool
import traceback

MAX_SIZE = 3 * 1024 * 1024
router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        content = await file.read()
        size = len(content)

        if size > MAX_SIZE:
            raise HTTPException(status_code=400, detail="File too large")

        query = """
            INSERT INTO files (filename, content)
            VALUES ($1, $2)
            RETURNING id;
        """

        async with db_pool.acquire() as conn:
            file_id = await conn.fetchval(query, file.filename, content)

        return {"id": file_id}

    except HTTPException:
        raise
    
    except Exception as e:
        return {"error": "Upload failed", "message": str(e), "trace": traceback.format_exc()}
