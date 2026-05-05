from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter(tags=["pages"])

# Templates directory is in ash-web/templates
# Path(__file__) is ash-web/backend/pages.py
TEMPLATES_DIR = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

@router.get("/", response_class=HTMLResponse)
async def landing(request: Request):
    """Serve the landing page."""
    return templates.TemplateResponse(request=request, name="index.html")

@router.get("/pricing", response_class=HTMLResponse)
async def pricing_page(request: Request):
    """Serve the pricing page."""
    return templates.TemplateResponse(request=request, name="pricing.html")

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    """Serve the login page."""
    return templates.TemplateResponse(request=request, name="login.html")

@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    """Serve the register page."""
    return templates.TemplateResponse(request=request, name="register.html")
