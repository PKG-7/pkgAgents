FROM python:3.11-slim

WORKDIR /app

# Установка необходимых пакетов
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Копируем все файлы проекта
COPY . .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт для API
EXPOSE 8000

# Настройка переменных окружения по умолчанию
ENV PYTHONUNBUFFERED=1

# Запуск приложения
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"] 