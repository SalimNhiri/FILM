from typing import Optional, Any,List
from datetime import datetime

from pydantic import BaseModel, EmailStr


class Profil(BaseModel):
    id: str
    user_id: str
    position: str
    titre : str
    companie : str
    email : EmailStr
    #tech : List[str]
    linkedin : str
    github : str
    creation : int = int(datetime.timestamp(datetime.utcnow()))
