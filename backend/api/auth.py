from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["auth"])

@router.post("/login")
async def api_login(data: dict):
    """Mock login API."""
    return {"status": "success", "message": "Logged in successfully", "user": data.get("email")}

@router.post("/register")
async def api_register(data: dict):
    """Mock register API."""
    return {"status": "success", "message": "Registered successfully", "user": data.get("email")}
