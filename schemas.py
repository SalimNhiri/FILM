from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

def individual_movie(film):
    return {
        "id": str(film["_id"]),
        "titre" : film["titre"],
        "url": film["url"],
        "photo" : film["photo"],
        "added_by": film["added_by"]
    }
    
def all_movies(films):
    return [individual_movie(film) for film in films]



def individual_user(user):
    return {
        "id": str(user["_id"]),
        "email" : user["email"],
        "name": user["name"],
        "photo" : user["photo"]
    }
    
def all_users(users):
    return [individual_user(user) for user in users]

    
class Userlogin(BaseModel):
    email : EmailStr
    password : str
    
class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None
    
    
    