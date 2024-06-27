from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

#################
# moovie
##################
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
    
#################
# profil
##################
def individual_profil(profil):
    return {
        "id": str(profil["_id"]),
        "titre" : profil["titre"],
        "position": profil["position"],
        "companie" : profil["companie"],
        "email": profil["email"],
        "linkedin": str(profil["linkedin"]),
        "github" : profil["github"],

    }
    
def all_profil(profils):
    return [individual_profil(profil) for profil in profils]

#################
# user
##################
def individual_user(user):
    return {
        "id": str(user["_id"]),
        "email" : user["email"],
        "name": user["name"],
        "photo" : user["photo"]
    }
    
def all_users(users):
    return [individual_user(user) for user in users]
    
#################
# MODELS 
##################
    
class Userlogin(BaseModel):
    email : EmailStr
    password : str
    
class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None
    
class ProfilData(BaseModel):
    id: str
    user_id: str
    titre: str
    position: str
    companie : str
    email : EmailStr
    #tech : List[str]
    linkedin : str
    github : str
    
