from fastapi import FastAPI

from routers import films, users, auth, profils
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
app.include_router(auth.profils)

@app.get("/")
async def root():
    return {"message": "Movie API"}
