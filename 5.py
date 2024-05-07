import requests
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
current_time = datetime.now()


@app.route('/fnl_pl/rfid/api/transfer/in', methods=['POST'])
def transfer_in():
    try:
        # Get JSON data from the request
        received_data = request.json
        print("1Current time:", current_time)
        print('1从收到rfid过来的数据received data:', received_data)

        # Process the received data
        payloads = []  # 存放要发送的数据
        for item in received_data:
            uuid = item['uuid']
            sn = item['sn']
            data = item['data']

            # Check if uuid is a specific value, if yes, return success without making a request
            if sn == "in-start":
                print("2Current time:", current_time)
                print('2收到了rfid,Satart-in的数据')
                return jsonify({"msg": "success", "state": "true"})

            # Prepare data for the second API
            payload_data = []
            for entry in data:
                payload_entry = {
                    "rfidNumber": entry['rfidNumber'],
                    "operator": entry['operator'],
                    "warehouse": entry['warehouse'],
                    "status": "OK",
                    "location": "A01"
                }
                payload_data.append(payload_entry)

            payload = {
                "uuid": uuid,
                "type": "in-return",
                "sn": sn,
                "data": payload_data
            }

            payloads.append(payload)  # 将准备好的数据添加到数组中

        # Make a POST request to the second API with all payloads at once
        response = requests.post('http://localhost:3000/api/transfer-out', json=payloads)

        # Check if the request was successful
        print("3Current time:", current_time)
        print('3发送给wms的payload', payloads)
        print()
        print("4Current time:", current_time)
        print('4接收到新接口给的反馈', response.text)
        if response.ok:
            print("5Current time:", current_time)
            print("5Successfully transferred data")
            return jsonify({"msg": "success", "state": "true"})
        else:
            print("6Current time:", current_time)
            print("6Failed to transfer data")
            print("7Current time:", current_time)
            print("7Error message:", response.text)
            return jsonify({"msg": "error", "state": "false"})

    except Exception as e:
        print("error", str(e))
        return jsonify({"msg": "error", "state": "false"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
