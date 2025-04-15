import sqlite3

# Подключаемся к БД (если файла нет — он создастся)
conn = sqlite3.connect('Tasks.db')
cursor = conn.cursor()

# Создаём таблицу "users"
cursor.execute('''
    CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- автоинкрементный ID
    title TEXT NOT NULL,                  -- заголовок задачи
    description TEXT,                     -- описание
    is_done BOOLEAN DEFAULT FALSE,        -- выполнена ли задача
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- дата создания
)
''')

# Сохраняем изменения
conn.commit()