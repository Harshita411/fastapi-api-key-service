from pydantic import BaseModel
from datetime import datetime

class APIKeyCreateResponse(BaseModel):
    key: str
    created_at: datetime