from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import upload, history  # add insights, process if needed
from database import lifespan
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI(lifespan=lifespan)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(upload.router)
app.include_router(history.router)
# app.include_router(insights.router)
# app.include_router(process.router)
