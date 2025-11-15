from fastapi import FastAPI
from routes import upload, history, insights, process
from database import lifespan

app = FastAPI(lifespan=lifespan)

# Routers
app.include_router(upload.router)
app.include_router(history.router)
app.include_router(insights.router)
app.include_router(process.router)
