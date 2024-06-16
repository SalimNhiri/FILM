
from fastapi import  HTTPException, APIRouter, Depends
from pydantic import BaseModel
from bson.objectid import ObjectId
from models.film import Film
from typing import Dict
from datetime import datetime

from configurations import collection_film
from schemas import all_movies,individual_movie
import oauth2

router = APIRouter(
    prefix = "/films",
    tags=["films"],
    responses={404:{"description":"Introuvable"}}
    
)


@router.get("/")
async def read_root( current_user: int = Depends(oauth2.get_current_active_user)):
    data = collection_film.find()
    return all_movies(data)

@router.post("/")
async def create_movie(film:Film,current_user: int = Depends(oauth2.get_current_active_user) ):
    try : 
        user_email = current_user['email']
        movie_toadd = dict(film)
        movie_toadd["added_by"] = user_email
        print(movie_toadd)
        resp = collection_film.insert_one(movie_toadd)
        return {
            "status_code":200,
            "id": str(resp.inserted_id)
        }
    except Exception as e:
        return HTTPException(status_code=500,detail="Une erreur est survenue  : %s"%e)

@router.get("/title/{titre}")
async def get_movie_by_name(titre: str):
    try:
        
        existing_movie = collection_film.find_one({"titre": {"$regex": titre, "$options": "i"}})
        if not existing_movie:
            return HTTPException(status_code=404, detail="Ce film n'existe pas dans la base")
        
        
        return {"status_code":200, "message":individual_movie(existing_movie)}
    except Exception as e:
        print(e)
        return HTTPException(status_code=500,detail="Une erreur est survenue  : %s"%e)
    

@router.put("/{movie_id}")
async def update_movie(movie_id: str,uptaded_movie:Film):
    try:
        id = ObjectId(movie_id)
        existing_movie = collection_film.find_one({"_id":id})
        if not existing_movie:
            return HTTPException(status_code=404, detail="Ce film n'existe pas dans la base")
        uptaded_movie.creation = datetime.timestamp(datetime.utcnow())
        resp = collection_film.update_one({"_id":id},{"$set":dict(uptaded_movie)})
        return {"status_code":200, "message":"le film a été mis a jour"}
    except Exception as e:
        print(e)
        return HTTPException(status_code=500,detail="Une erreur est survenue  : %s"%e)
    
@router.delete("/{movie_id}")
async def update_movie(movie_id: str,uptaded_movie:Film):
    try:
        id = ObjectId(movie_id)
        existing_movie = collection_film.find_one({"_id":id})
        if not existing_movie:
            return HTTPException(status_code=404, detail="Ce film n'existe pas dans la base")
        
        resp = collection_film.delete_one({"_id":id})
        return {"status_code":200, "message":"le film a été supprimé"}
    except Exception as e:
        print(e)
        return HTTPException(status_code=500,detail="Une erreur est survenue  : %s"%e)