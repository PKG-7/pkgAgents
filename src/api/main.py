from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.openapi.utils import get_openapi
import logging

from .routes import router

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="PKG Agents API",
    description="""
    🤖 API для взаимодействия с различными AI агентами

    ### Возможности
    * 💬 Базовый чат для простого общения
    * 🛠️ Продвинутый чат с доступом к инструментам
    * 🚫 Модерация сообщений

    ### Как использовать
    1. Выберите нужный эндпоинт из списка слева
    2. Нажмите "Try it out"
    3. Введите сообщение
    4. Нажмите "Execute"
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
    openapi_tags=[
        {
            "name": "Базовые чаты",
            "description": "Простые чат-боты без специальных возможностей"
        },
        {
            "name": "Продвинутые чаты",
            "description": "Чат-боты с расширенными возможностями и доступом к инструментам"
        },
        {
            "name": "Модерация",
            "description": "Инструменты для проверки и модерации контента"
        },
        {
            "name": "internal",
            "description": "Внутренние эндпоинты",
            "hidden": True
        }
    ]
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

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="src/api/static"), name="static")

app.include_router(router)

# Кастомный OpenAPI endpoint
@app.get("/api-docs/openapi.json", tags=["internal"])
async def get_openapi_json():
    return get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
        tags=app.openapi_tags
    )

# Elements UI
@app.get("/reference", response_class=HTMLResponse, tags=["internal"])
async def get_documentation():
    return """
    <!doctype html>
    <html lang="en" data-theme="dark">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>PKG Agents API Reference</title>
        <script src="https://unpkg.com/@stoplight/elements/web-components.min.js"></script>
        <link rel="stylesheet" href="https://unpkg.com/@stoplight/elements/styles.min.css">
        <link rel="stylesheet" href="/static/styles.css">
      </head>
      <body style="height: 100vh; margin: 0;">
        <button id="theme-toggle" aria-label="Переключить тему">
          <svg class="sun" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <path d="M12 18C8.68629 18 6 15.3137 6 12C6 8.68629 8.68629 6 12 6C15.3137 6 18 8.68629 18 12C18 15.3137 15.3137 18 12 18ZM12 16C14.2091 16 16 14.2091 16 12C16 9.79086 14.2091 8 12 8C9.79086 8 8 9.79086 8 12C8 14.2091 9.79086 16 12 16ZM11 1H13V4H11V1ZM11 20H13V23H11V20ZM3.51472 4.92893L4.92893 3.51472L7.05025 5.63604L5.63604 7.05025L3.51472 4.92893ZM16.9497 18.364L18.364 16.9497L20.4853 19.0711L19.0711 20.4853L16.9497 18.364ZM19.0711 3.51472L20.4853 4.92893L18.364 7.05025L16.9497 5.63604L19.0711 3.51472ZM5.63604 16.9497L7.05025 18.364L4.92893 20.4853L3.51472 19.0711L5.63604 16.9497ZM23 11V13H20V11H23ZM4 11V13H1V11H4Z"/>
          </svg>
          <svg class="moon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="display: none;">
            <path d="M10 7C10 10.866 13.134 14 17 14C18.9584 14 20.729 13.1957 21.9995 11.8995C22 11.933 22 11.9665 22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C12.0335 2 12.067 2 12.1005 2.00049C10.8043 3.27098 10 5.04157 10 7ZM4 12C4 16.4183 7.58172 20 12 20C15.0583 20 17.7158 18.2839 19.062 15.7621C18.3945 15.9187 17.7035 16 17 16C12.0294 16 8 11.9706 8 7C8 6.29648 8.08133 5.60547 8.2379 4.938C5.71611 6.28423 4 8.94174 4 12Z"/>
          </svg>
        </button>
        <elements-api
          apiDescriptionUrl="/api-docs/openapi.json"
          router="hash"
          layout="sidebar"
          appearance="dark"
        />
        <script src="/static/theme.js"></script>
      </body>
    </html>
    """ 