from fastapi import APIRouter
from app.services.key_service import generate_api_key
from app.schemas.api_key import APIKeyCreateResponse

router = APIRouter()

@router.post("/keys", response_model=APIKeyCreateResponse)
def create_api_key():
    return generate_api_key()