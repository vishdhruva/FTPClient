import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(5)
print("Holding for incoming connections ...")

while True:
    clientsocket, address = s.accept()
    print(f"Conection from {address} has been established")
    clientsocket.send(bytes("Welcome to the server", "utf-8"))
