from fastapi import FastAPI, HTTPException, APIRouter,status,Depends
from configurations import collection_users
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from schemas import all_users, individual_user
import schemas

import utils, oauth2

router = APIRouter(tags=['Authentification'])


    
@router.post('/login', response_model=schemas.Token)
async def login(user_credentials :  OAuth2PasswordRequestForm = Depends()):
    mail = user_credentials.username
    print(mail)
    existing_user = collection_users.find_one({"email":mail})
    
    existing_user_password = existing_user["password"]

    if not existing_user:
        return HTTPException(status_code=404, detail="L'utilisateur n'existe pas")
    
    if not utils.verify(user_credentials.password,existing_user_password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="mot de passe incorect")
    
    access_token = oauth2.create_access_token(data={"user_id":mail})
   
    return {"status_code":200, "access_token":access_token, "token_type":"bearer"}
    