import socket
import threading
import random

def onNewClient(client, address):
    print("Connected to client")
    while True:
        try:
            msg = client.recv(1024)
            msg = msg.decode('utf-8')
            print(address, ' >> ', msg)
            battery = random.randint(0, 1000)
            speed = random.randint(0, 20)
            print(battery)
            print(speed)
            msg = str(speed) + "," + str(battery)
            client.sendall(msg.encode())
        except ConnectionAbortedError:
            print("Connection Closed")
            break
            
s = socket.socket()
host = "127.0.0.1"
port = 50000

battery = random.randint(0, 1000)
speed = random.randint(0, 20)
msg = str(speed) + "," + str(battery)

print(battery)
print(speed)

s.bind((host, port))
s.listen(5)

print("Server started, listening")

while True:
    c, addr = s.accept()
    clientThread = threading.Thread(target=onNewClient, args=(c, addr))
    clientThread.start()