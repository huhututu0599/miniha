from flask import Flask, jsonify, request
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/post_select_data', methods=['POST'])
def get_users():

    # data1 = request.json
    # id1 = data1.get('id')
    # print(data1)
    # 连接到 SQLite 数据库
    conn = sqlite3.connect('example.db')

    # 创建游标对象
    cursor = conn.cursor()

    # 执行查询语句
    # cursor.execute("SELECT * FROM users where id =?",id1)
    cursor.execute("SELECT * FROM users")
    # 获取查询结果
    rows = cursor.fetchall()

    # 将查询结果封装成 JSON 格式
    users = [{'id': row[0], 'wendu': row[1], 'shidu': row[2]} for row in rows]

    # 关闭游标对象和数据库连接
    cursor.close()
    conn.close()


    # 返回 JSON 格式的数据
    return jsonify(users)
    # data = {
    #     "id": 1,
    #     "shidu": "2234",
    #     "wendu": "21344"
    # }
    # # formatted_string = '{{"id": {},"shidu": {},"wendu": "{}"}}'.format(
    # #     data['id'],
    # #     data['shidu'],
    # #     data['wendu']
    # # )
    # return jsonify(data)


@app.route('/post_RecData', methods=['POST'])
def RecData():
    # 连接到 SQLite 数据库（如果不存在，则会创建一个新的数据库）
    conn = sqlite3.connect('example.db')

    # 创建游标对象
    cursor = conn.cursor()

    # 从 POST 请求中获取 JSON 数据
    data = request.json

    # 处理接收到的数据
    # 这里假设接收到的数据是一个包含 "name" 和 "age" 字段的 JSON 对象
    wendu = data.get('wendu')
    shidu = data.get('shidu')

    # 创建一个表格（如果表格不存在）
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (id INTEGER PRIMARY KEY, 温度 TEXT, 湿度 TEXT)''')

    # 准备要插入的数据
    user_data = [
        (wendu, shidu)
    ]

    # 执行 INSERT 语句插入数据
    cursor.executemany('INSERT INTO users (温度, 湿度) VALUES (?, ?)', user_data)

    # 提交更改
    conn.commit()

    # 关闭游标对象和数据库连接
    cursor.close()
    conn.close()

    # 返回 JSON 格式的数据
    return jsonify('ok')

if __name__ == '__main__':
    app.run(debug=True)
