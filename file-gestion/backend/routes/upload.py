from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, FastAPI
from models import Upload
import logging
import base64  # <-- import here at the top

router = APIRouter()
logger = logging.getLogger(__name__)

MAX_SIZE = 3 * 1024 * 1024  # 3MB

def get_db_pool(app: FastAPI = Depends()):
    pool = getattr(app.state, "db_pool", None)
    if pool is None:
        raise RuntimeError("DB pool is not initialized!")
    return pool

@router.post("/upload", response_model=Upload)
async def upload_file(
    file: UploadFile = File(...),
    parsed_json: dict | None = None,
    metadata: dict | None = None,
    pool=Depends(get_db_pool)
):
    content = await file.read()
    if len(content) > MAX_SIZE:
        raise HTTPException(status_code=400, detail="File too large")

    query = """
        INSERT INTO uploads (filename, content, mimetype, parsed_json, metadata)
        VALUES ($1, $2, $3, $4, $5)
        RETURNING id, filename, content, mimetype, parsed_json, metadata, uploaded_at;
    """

    async with pool.acquire() as conn:
        row = await conn.fetchrow(query, file.filename, content, file.content_type, parsed_json, metadata)

    # Convert to Upload model, encode content to Base64 for JSON serialization
    upload = Upload(
        id=row["id"],
        filename=row["filename"],
        content=base64.b64encode(row["content"]).decode() if row["content"] else None,
        mimetype=row["mimetype"],
        parsed_json=row["parsed_json"],
        metadata=row["metadata"],
        uploaded_at=row["uploaded_at"]
    )

    logger.debug(f"Created upload: {upload}")
    return upload
