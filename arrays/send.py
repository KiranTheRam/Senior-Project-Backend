import socket
import pickle

UDP_IP = "127.0.0.1"
UDP_PORT = 5001
a = ['SensorID', 'Distance', 1234]
MESSAGE = pickle.dumps(a)
print("Sending array to", UDP_IP, ":", UDP_PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
