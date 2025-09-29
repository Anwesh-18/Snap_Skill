from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.auth import auth

app = FastAPI()

app.include_router(auth)