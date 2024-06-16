
from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from bson.objectid import ObjectId
from models.user import User
import utils 
from typing import Dict
from datetime import datetime

from configurations import collection_users
from schemas import all_users, individual_user




router = APIRouter(
    prefix = "/Users",
    tags=["Users"],
    responses={404:{"description":"Introuvable"}}
    
)


@router.get("/")
async def read_root():
    data = collection_users.find()
    return all_users(data)

@router.get("/Profil/{user_id}")
async def get_user(user_id:str):
    id = ObjectId(user_id)
    resp = collection_users.find_one({"_id":id})
    
    return { "status_code" : 200,
            "message" : individual_user(resp)}

@router.post("/")
async def create_user(user:User ):
    try : 
        
        #hash the password
        hashed_password = utils.hash(user.password)
        user.password = hashed_password
        
        resp = collection_users.insert_one(dict(user))
        return {
            "status_code":200,
            "id": str(resp.inserted_id)
        }
    except Exception as e:
        return HTTPException(status_code=500,detail="Une erreur est survenue  : %s"%e)

