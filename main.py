import sqlite3

# 连接到 SQLite 数据库（如果不存在，则会创建一个新的数据库）
conn = sqlite3.connect('example.db')

# 创建游标对象
cursor = conn.cursor()

# 创建一个表格（如果表格不存在）
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# 准备要插入的数据
user_data = [
    ('Alice', 30),
    ('Bob', 25),
    ('Charlie', 35)
]

# 执行 INSERT 语句插入数据
cursor.executemany('INSERT INTO users (name, age) VALUES (?, ?)', user_data)

# 提交更改
conn.commit()

# 关闭游标对象和数据库连接
cursor.close()
conn.close()
