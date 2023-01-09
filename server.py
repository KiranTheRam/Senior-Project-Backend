# UDP Listener
import socket


def UDP_Listener():
    # Setting up address, port, and buffer values
    localIP = "127.0.0.1"
    localPort = 4455
    bufferSize = 1024

    # Message to be sent to a client that connects
    msgFromServer = "You have connected to the server on localhost"

    # Turning the message into bytes
    bytesToSend = str.encode(msgFromServer)

    # Create a UDP datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # UDPServerSocket.sendto(bytes("Hello there", "utf-8"), ("127.0.0.1", 4455))

    # Bind the socket to the IP and Port specified above
    UDPServerSocket.bind((localIP, localPort))

    print("UDP server is operational, listening for client. . .")

    # Listen for incoming datagrams
    while (True):
        # Receive _____
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        # Gathering message and address from the client
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP = "Client IP Address:{}".format(address)

        print(clientMsg)
        print(clientIP)

        # Sending reply to client
        UDPServerSocket.sendto(bytesToSend, address)

if __name__ == '__main__':
    print('Hello')
    UDP_Listener()

