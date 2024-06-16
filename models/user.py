from typing import Optional, Any
from datetime import datetime

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    photo: str
    creation : int = int(datetime.timestamp(datetime.utcnow()))