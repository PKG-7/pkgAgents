# Pydantic Agents

Проект для работы с различными агентами на основе Pydantic.

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
└── requirements.txt      # Зависимости проекта
```

## 🚀 Установка и запуск

1. Создайте виртуальное окружение и активируйте его:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Установите зависимости:

```powershell
pip install -r requirements.txt
```

3. Создайте файл `.env` с необходимыми переменными окружения

## 💻 Запуск веб-интерфейса

Для запуска веб-интерфейса выполните:

```powershell
python web\server.py
```

Веб-интерфейс будет доступен по адресу: http://localhost:3000

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

API построено на FastAPI и доступно после запуска сервера.
Документация Swagger UI доступна по адресу: http://localhost:8000/docs
