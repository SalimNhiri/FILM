from fastapi import FastAPI

from routers import films, users, auth


app = FastAPI()

        
app.include_router(users.router) 
app.include_router(films.router)
app.include_router(auth.router)

