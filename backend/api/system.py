from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path

# DIST_DIR is my_AItools/dist
# Path(__file__) is ash-web/backend/api/system.py
DIST_DIR = Path(__file__).parent.parent.parent.parent / "dist"

router = APIRouter(tags=["system"])

@router.get("/download")
async def download():
    """Serve the latest Ashborn IDE bundle."""
    bundle = DIST_DIR / "ashborn-ide-linux.tar.gz"
    if bundle.exists():
        return FileResponse(
            str(bundle),
            media_type="application/gzip",
            filename="ashborn-ide-linux.tar.gz",
        )
    return {"status": "error", "message": "Build not available yet. Check back soon!"}

@router.get("/api/stats")
async def stats():
    """Return basic project stats for the landing page."""
    return {
        "version": "0.1.0",
        "tools": 10,
        "brain_modules": 4,
        "api_endpoints": 12,
    }
