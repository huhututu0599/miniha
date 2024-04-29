
# btle_dos_attack.py

import asyncio
from bleak import BleakScanner, BleakClient

# Callback function triggered when a BLE device is detected
# 检测到BLE设备时触发回调功能
def detection_callback(device, advertisement_data):
    """Callback for detected devices during scanning."""
    data = advertisement_data[2]
    if '0000fcd2-0000-1000-8000-00805f9b34fb' in data:
        print(advertisement_data)
        print("名称:", device.name, end = "\t")
        print("地址:", device.address)
        s = data['0000fcd2-0000-1000-8000-00805f9b34fb']
        a = [hex(x) for x in s]
        print(a)
        print("温度:", (int(a[3], 16) * 256 + int(a[2], 16)) / 100)
        print("湿度:", (int(a[6], 16) * 256 + int(a[5], 16)) / 100)
        print("电压:", (int(a[9], 16) * 256 + int(a[8], 16)) / 1000)
        print("电量:", int(a[11], 16))


async def run():
    """Main asynchronous function to handle BLE operations."""
    
    # Initialize the scanner with the detection callback
    #使用检测回调初始化扫描仪
    scanner = BleakScanner(detection_callback=detection_callback)
    
    # Start scanning for devices
    #开始扫描设备
    await scanner.start()
    await asyncio.sleep(60)  # Scan for 10 seconds #扫描10秒
    await scanner.stop()
    
    # Retrieve and list the discovered devices
    #检索并列出发现的设备
    #
    #devices = await scanner.get_discovered_devices()
    #for i, device in enumerate(devices):
    #     print(f"{i + 1}. {device.name} ({device.address})")

# Initialize and start the asynchronous event loop
#初始化并启动异步事件循环



loop = asyncio.get_event_loop()
loop.run_until_complete(run())


'''
数据接收
service_data={'0000fcd2-0000-1000-8000-00805f9b34fb': b'@\x02\xd9\r\x03\xda\r\x0c\x06\x0c\x01`'}
'''
