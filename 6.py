import requests

# 定义请求的URL
url = 'http://localhost:8080/fnl_pl/rfid/api/transfer/in'

# 定义要发送的数据
data = [
    {
        "uuid": "1234521234711212",
        "type": "in",
        "sn": "in-12345672821212",
        "data": [
            {
                "rfidNumber": "ABCD1234CDEF5678FECD0088",
                "operator": "张三",
                "warehouse": "100990"
            },
            {
                "rfidNumber": "ABCD1234CDEF5678FECD0004",
                "operator": "张三",
                "warehouse": "10070"
            }
        ]
    }
]

# 发送POST请求
response = requests.post(url, json=data)

# 打印响应结果
print(response.text)
