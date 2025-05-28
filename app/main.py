from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routers.router import router

app = FastAPI()

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # agrega aquí los dominios de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)