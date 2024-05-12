import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost',8080))
server.listen(True)

print("Server started successfully")


connection,address = server.accept()
print(f"Client connected successfully at {address}")

while(True):
	received = connection.recv(1024).decode()
	print(f"Client saying: {received}")
	if not received:
		break	

	#if text is exit, then close
	if received.lower()=="exit":
		break

	message = input("Your text: ")
	connection.send(message.encode())

	if message.lower()=="exit":
		break

connection.close()
