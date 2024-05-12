import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost',8080))

print("Server connected successfully")


while(True):
	message = input("Your text: ")
	client.send(message.encode())

	#if text is exit then close
	if message.lower()=="exit":
		break
	
	received = client.recv(1024).decode()
	print(f"Server saying : {received} ")

	if not received:
		break
	
	if received.lower()=="exit":
		break
	
client.close()
