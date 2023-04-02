import json
import socket
import requests
import pickle

api_url = "https://bgpj1c.deta.dev/postroom"

UDP_IP = "127.0.0.1"
UDP_PORT = 5001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024)

    # Deserialize the data
    deserialized_data = pickle.loads(data)
    print("received message:", deserialized_data)

    room_info = '{"sensorID": ' + deserialized_data[0] + ', "distance": ' + deserialized_data[2] + ', "deviceID":' + deserialized_data[1] + '}'
    response = requests.post(api_url, json.loads(room_info))

    print(response.json())
    print("\n\n")
