"""
Ashborn Landing Page — FastAPI backend.
Serves the static site and provides a download endpoint.
"""

from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from backend.pages import router as pages_router
from backend.api.auth import router as auth_router
from backend.api.system import router as system_router

STATIC_DIR = Path(__file__).parent / "static"

app = FastAPI(title="Ashborn Landing Page", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include modular routers
app.include_router(pages_router)
app.include_router(auth_router)
app.include_router(system_router)

# Mount static assets AFTER routes so they don't shadow /download etc.
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=3000, reload=True)
