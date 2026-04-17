from fastapi import APIRouter, Depends
from app.api.deps import get_api_key

router = APIRouter()

@router.get("/protected")
def protected_route(api_key: str = Depends(get_api_key)):
    return {
        "message": "You accessed a protected route",
        "api_key_used": api_key
    }

@router.get("/profile")
def profile(api_key: str = Depends(get_api_key)):
    return {
        "message": "Profile data",
        "api_key": api_key
    }