FROM python:3.11-slim

WORKDIR /app

# Установка необходимых пакетов
RUN apt-get update && \
    apt-get install -y git curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Клонирование репозитория
RUN git clone https://github.com/PKG-7/pkgAgents.git .

# Обновляем requirements.txt
RUN sed -i '/pydantic-ai/d' requirements.txt && \
    sed -i 's/typing-extensions==4.5.0/typing-extensions>=4.12.2/' requirements.txt && \
    sed -i 's/pydantic==2.10.3/pydantic>=2.10.3/' requirements.txt

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порты для API и веб-интерфейса
EXPOSE 8000
EXPOSE 3000

# Создаем entrypoint скрипт
RUN echo '#!/bin/bash\n\
# Ждем немного перед запуском сервисов\n\
sleep 2\n\
\n\
# Запуск FastAPI в фоновом режиме\n\
echo "Запуск FastAPI сервера..."\n\
uvicorn src.api.main:app --host 0.0.0.0 --port 8000 &\n\
\n\
# Ждем запуска FastAPI\n\
sleep 5\n\
\n\
# Запуск веб-сервера\n\
echo "Запуск веб-интерфейса..."\n\
python web/server.py' > entrypoint.sh

RUN chmod +x entrypoint.sh

# Настройка переменных окружения по умолчанию
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["./entrypoint.sh"] 