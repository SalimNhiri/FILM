from fastapi import FastAPI

from routers import films, users, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
        
app.include_router(users.router) 
app.include_router(films.router)
app.include_router(auth.router)

app.get("/")
def root():
    return {"message": "Hello World pushing out to ubuntu"}