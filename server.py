import json
import socket
import requests
import re
from datetime import datetime

# UDP_IP = "127.0.0.1"
UDP_IP = "10.1.12.195"

UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

print("Listening...")
while True:
    data, addr = sock.recvfrom(128)

    decoded_data = data.decode("ISO-8859-1")
    #print(decoded_data)
    decoded_data = re.search("\{(.*?)\}", decoded_data)
    print("Received: %s" % decoded_data.group())
    json_value = json.loads(decoded_data.group())

    # Map values
    sensorID = json_value["sensorID"]
    deviceID = json_value["phoneID"]
    distance = json_value["distance"]

    print("\nMapped Values from JSON:")
    print("SensorID: " + sensorID)
    print("DeviceID: " + deviceID)
    print("Distance: " + distance)

    print("\nSending GET request for more info")
    api_url = "https://uwb-react-app-weuz.vercel.app/api/sensors/getbyid"
    # Body to be used in "get" request
    getSensorReq = '{"sensorID": \"' + sensorID + '\"}'
    response = requests.post(api_url, json.loads(getSensorReq))
    print(response.json())
    # Get the current date and time
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")

    # Mapping returned data tied to the sensor
    sensor_info = response.json()
    roomID = sensor_info[0]["roomID"]
    latitude = sensor_info[0]["latitude"]
    longitude = sensor_info[0]["longitude"]
    buildingID = sensor_info[0]["buildingID"]

    print("\nMapped Values from GET:")
    print("RoomID: " + roomID)
    print("Lat: " + latitude)
    print("Long: " + longitude)
    print("Time: " + current_time)
    print("BuildingID: " + buildingID)

    print("POSTing new information to DB")
    api_url = "https://uwb-react-app-weuz.vercel.app/api/roomreports/newreport"
    # Body to be used in POST request that updates room data
    room_info = '{ "tagID": "100", "buildingID": \"' + buildingID + '\", "roomID": \"' + roomID + '\", "lat": \"' + latitude + '\", "long": \"' + longitude + '\", "time": \"' + current_time + '\", "distance": \"' + distance + '\", "deviceID": \"' + deviceID + '\"} '
    print(room_info)
    response = requests.post(api_url, json.loads(room_info))
    print(response)
    print(response.json())

    print("_______________\n")
