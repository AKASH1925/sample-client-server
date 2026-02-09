import socket
server_socket = socket.socket(socket.AF_INET, 
socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 12345)) # Listen on port 12345
server_socket.listen(1) 
print("Server is listening...") 
conn, addr = server_socket.accept()
print(f"Connection established with {addr}") 
data = conn.recv(1024) 
print(f"Received: {data.decode()}") 
conn.send(b"Hello from server") 
conn.close()
server_socket.close()
