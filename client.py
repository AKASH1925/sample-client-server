import socket
client_socket = socket.socket(socket.AF_INET, 
socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345)) # Connect to the server
client_socket.send(b"Hello from client") 
response = client_socket.recv(1024) 
print(f"Received from Server: {response.decode()}") 
client_socket.close()

