﻿Проект To-do List

1) Создаем базу данных с таблицей tasks:
 - Запускаем скрипт db_create.py
 - Создастся файл Tasks.db
2) Устанавливаем библиотеки: pip install fastapi uvicorn sqlalchemy
3) Создаем API на FastAPI - скрипт main.py
 - Методы get, post, update, delete
4) Запускаем API:
 - uvicorn main:app --reload
 - Сервер запустится на http://127.0.0.1:8000.
 - Документация API:
  - Swagger UI: http://127.0.0.1:8000/docs
  - Redoc: http://127.0.0.1:8000/redoc
