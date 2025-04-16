import sqlite3

# 1. Подключение к БД (файл my_database.db будет создан автоматически)
conn = sqlite3.connect('my_database.db')

# 2. Создание курсора для выполнения SQL-запросов
cursor = conn.cursor()

# 3. Создание таблицы
cursor.execute('''
    CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- автоинкрементный ID
    title TEXT NOT NULL,                  -- заголовок задачи
    description TEXT,                     -- описание
    is_done BOOLEAN DEFAULT FALSE,        -- выполнена ли задача
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- дата создания
)
''')

# 4. Сохранение изменений
conn.commit()

# 5. Закрытие соединения
conn.close()