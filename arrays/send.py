import keyboard  # using module keyboard
import socket
import pickle
import random

UDP_IP = "127.0.0.1"
UDP_PORT = 5001

# Establish Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    if keyboard.read_key() == "q":
        exit(-1)

    if keyboard.read_key() == "s":
        # Create a random distance and add to list
        distance = round(random.uniform(0, 20), 2)
        packet_content = ['SensorID', "PhoneID", distance]

        # Serialize the array
        MESSAGE = pickle.dumps(packet_content)

        # Send the packet
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

        print("Sending array to " + UDP_IP + ":" + str(UDP_PORT))
        continue
