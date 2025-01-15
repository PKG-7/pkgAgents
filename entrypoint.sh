#!/bin/bash

# Ждем немного перед запуском сервисов
sleep 2

# Запуск FastAPI в фоновом режиме
echo "Запуск FastAPI сервера..."
uvicorn src.api.main:app --host 0.0.0.0 --port 8000 &

# Ждем запуска FastAPI
sleep 5

# Запуск веб-сервера
echo "Запуск веб-интерфейса..."
python web/server.py 