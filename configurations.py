
from urllib.parse import quote_plus

from dotenv import load_dotenv

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import os

load_dotenv()
passwordvalue = os.getenv("mongopswd")

password = quote_plus(passwordvalue)
print(password)
uri = "mongodb+srv://salimnhiri19:%s@cluster0.cw4yn74.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"%password

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    db = client.Film_db
    collection_film  = db["FILMS"]
    collection_users  = db["USERS"]
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)