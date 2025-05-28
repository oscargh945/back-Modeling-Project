from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routers.router import router

app = FastAPI()

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],  # agrega aquí los dominios de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)