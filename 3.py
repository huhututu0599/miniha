import json

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/fnl_pl/rfid/api/transfer/in', methods=['POST'])
def transfer_in():
    try:
        # Get JSON data from the request
        received_data = request.json
        print('1从收到rfid过来的数据received data:', received_data)
        # Process the received data
        for item in received_data:
            uuid = item['uuid']
            sn = item['sn']
            data = item['data']

            # Check if uuid is a specific value, if yes, return success without making a request
            if sn == "in-start":
                print('2收到了rfid,Satart-in的数据')
                return jsonify({"msg": "success","state": "true"})

            # Prepare data for the second API
            payload = {
                "uuid": uuid,
                "type": "in-return",
                "sn": sn,
                "data": []
            }

            # Process each rfidNumber entry in the received data
            for entry in data:
                # Add additional fields or modify existing ones if needed
                entry.update({
                    "status": "OK",
                    "warehouse": "10060",
                    "location": "A01"
                })
                payload['data'].append(entry)
            print('3发送给wms的payload',json.dump(payload))
            # Make a POST request to the second API
            #response = requests.post('http://z-iot.asuscomm.com:8082/api/transfer-out', json=[payload])
            response = requests.post('http://localhost:3000/api/transfer-out', json=[payload])

            # Check if the request was successful
            print('4接收到新接口给的反馈',response.text)
            if response.ok:
                print(f"5Successfully transferred data for uuid: {uuid}, sn: {sn}")
            else:
                print(f"6Failed to transfer data for uuid: {uuid}, sn: {sn}")
                print(f"7Error message: {response.text}")

        return jsonify({"msg": "success", "state": "true"})
    except Exception as e:
        print("error", str(e))
        return jsonify({"msg": "error", "state": "false"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
