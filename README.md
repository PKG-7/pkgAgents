# Pydantic Agents

Проект для работы с различными агентами на основе Pydantic.

## 🚀 Быстрый старт

### Клонирование репозитория

```powershell
git clone https://github.com/PKG-7/pkgAgents.git
cd pkgAgents
```

## 📁 Структура проекта

```
├── src/                    # Исходный код
│   ├── agents/            # Реализации агентов
│   ├── api/               # FastAPI приложение
│   └── stormlabs/         # Дополнительные модули
├── web/                   # Веб-интерфейс
│   ├── server.py         # Веб-сервер
│   └── index.html        # Главная страница
├── test.py               # Тестовые примеры
├── api.py                # API endpoints
├── Dockerfile            # Конфигурация Docker
├── docker-compose.yml    # Конфигурация Docker Compose
└── requirements.txt      # Зависимости проекта
```

## 🛠 Установка и запуск

### Через Docker (рекомендуется)

1. Убедитесь, что у вас установлен [Docker](https://www.docker.com/products/docker-desktop/) и Docker Compose

2. Создайте файл `.env` в корне проекта:

```
OPENAI_API_KEY=your_api_key_here
```

3. Соберите и запустите контейнеры:

```powershell
docker-compose up --build
```

После запуска будут доступны:

-   API: http://localhost:8000
-   Веб-интерфейс: http://localhost:3000

Для остановки сервисов:

```powershell
docker-compose down
```

### Локальный запуск (для разработки)

1. Создайте виртуальное окружение и активируйте его:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Установите зависимости:

```powershell
pip install -r requirements.txt
```

3. Создайте файл `.env` с вашим API ключом OpenAI:

```
OPENAI_API_KEY=your_api_key_here
```

4. Запустите API сервер:

```powershell
uvicorn src.api.main:app --reload
```

5. В отдельном терминале запустите веб-интерфейс:

```powershell
python web\server.py
```

## 🧪 Тестирование

В файле `test.py` находятся примеры использования различных агентов:

-   AgentIsRude - проверка на грубость
-   AgentBasic - базовый агент
-   AgentWithTools - агент с инструментами

Для запуска тестов выполните:

```powershell
python test.py
```

## 📚 API Documentation

API построено на FastAPI. После запуска сервера документация доступна по адресам:

-   Swagger UI: http://localhost:8000/docs
-   ReDoc: http://localhost:8000/redoc

## 🔑 Переменные окружения

Проект требует следующие переменные окружения в файле `.env`:

-   `OPENAI_API_KEY` - ваш API ключ OpenAI
