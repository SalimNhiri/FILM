from fastapi import  HTTPException, APIRouter, Depends
from pydantic import BaseModel
from bson.objectid import ObjectId
from models.profil import Profil
from typing import Dict
from datetime import datetime

from configurations import collection_profils
from schemas import all_profil,individual_profil
import oauth2

router = APIRouter(
    prefix = "/profils",
    tags=["profil"],
    responses={404:{"description":"Introuvable"}}
    
)


@router.get("/")
async def read_root( current_user: int = Depends(oauth2.get_current_active_user)):
    data = collection_profils.find()
    return all_profil(data)

@router.post("/")
async def create_profil(profil:Profil,current_user: int = Depends(oauth2.get_current_active_user) ):
    try : 
        user_email = current_user['email']
        profil_toadd = dict(profil)
        profil_toadd["user_id"] = user_email
        print(profil_toadd)
        resp = collection_profils.insert_one(profil_toadd)
        return {
            "status_code":200,
            "id": str(resp.inserted_id)
        }
    except Exception as e:
        return HTTPException(status_code=500,detail="Une erreur est survenue  : %s"%e)

@router.get("/title/{titre}")
async def get_profil_by_name(titre: str):
    try:
        
        existing_profil = collection_profils.find_one({"titre": {"$regex": titre, "$options": "i"}})
        if not existing_profil:
            return HTTPException(status_code=404, detail="Ce profil n'existe pas dans la base")
        
        
        return {"status_code":200, "message":individual_profil(existing_profil)}
    except Exception as e:
        print(e)
        return HTTPException(status_code=500,detail="Une erreur est survenue  : %s"%e)
    

@router.put("/{profil_id}")
async def update_movie(profil_id: str,uptaded_profil:Profil):
    try:
        id = ObjectId(profil_id)
        existing_profil = collection_profils.find_one({"_id":id})
        if not existing_profil:
            return HTTPException(status_code=404, detail="Ce profil n'existe pas dans la base")
        uptaded_profil.creation = datetime.timestamp(datetime.utcnow())
        resp = collection_profils.update_one({"_id":id},{"$set":dict(uptaded_profil)})
        return {"status_code":200, "message":"le film a été mis a jour"}
    except Exception as e:
        print(e)
        return HTTPException(status_code=500,detail="Une erreur est survenue  : %s"%e)
    
@router.delete("/{profil_id}")
async def update_movie(profil_id: str,uptaded_profil:Profil):
    try:
        id = ObjectId(profil_id)
        existing_profil = collection_profils.find_one({"_id":id})
        if not existing_profil:
            return HTTPException(status_code=404, detail="Ce profil n'existe pas dans la base")
        
        resp = collection_profils.delete_one({"_id":id})
        return {"status_code":200, "message":"le profil a été supprimé"}
    except Exception as e:
        print(e)
        return HTTPException(status_code=500,detail="Une erreur est survenue  : %s"%e)
