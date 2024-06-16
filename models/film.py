from typing import Optional, Any
from datetime import datetime

from pydantic import BaseModel, EmailStr


class Film(BaseModel):
    titre: str
    url: str
    photo: str
    added_by : EmailStr
    creation : int = int(datetime.timestamp(datetime.utcnow()))