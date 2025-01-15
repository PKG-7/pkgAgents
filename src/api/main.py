from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from .routes import router

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Agents API",
    description="API для взаимодействия с AI агентами",
    version="1.0.0"
)

# Настройка CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router) 