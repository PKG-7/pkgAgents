FROM python:3.11-slim

WORKDIR /app

# Установка необходимых пакетов
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Копируем файлы проекта
COPY requirements.txt .
COPY src/ ./src/

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт для API
EXPOSE 8000

# Создаем entrypoint скрипт
RUN echo '#!/bin/bash\n\
echo "Запуск FastAPI сервера..."\n\
uvicorn src.api.main:app --host 0.0.0.0 --port 8000' > entrypoint.sh

RUN chmod +x entrypoint.sh

# Настройка переменных окружения по умолчанию
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["./entrypoint.sh"] 