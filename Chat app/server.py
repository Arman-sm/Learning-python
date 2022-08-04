import socket

def receive(conn):
	result = b""
	while True:
		packet = conn.recv(1024)
		result = result + packet
		conn.send(b"%%ACK%%")
		if packet[-7:] == b"%%END%%":
			if result[:-7] == b"%%EMT%%":
				return ""
			return result.decode()[:-7]
			
def send(conn, txt):
	if txt == "":
		result = [b"%%EMT%%%%END%%"]
	else:
		#Encoding the text into binary
		result = txt.encode()
		#Splitting the encoded text into smaller packets to send if needed so we can send texts with any size
		result = [result[group*1017:(group+1)*1017] for group in range(int(len(result)/1017 if len(result)%1017 == 0 else len(result)//1017+1))]
		#1024 - 7 => packet size - end phrase length
		result[len(result)-1] = result[len(result)-1] + "%%END%%".encode()
	#Sending packets one by one
	for packet in result:
		# Send the message to the client
		conn.send(packet)
		#Waiting for the other side to acknowledge
		while True:
			if (conn.recv(1024)) == b"%%ACK%%":
				break

# Socket object             
s = socket.socket()

#Port and IP  
s.bind((socket.gethostname(), 60417))           
s.listen()                     
print('Server listening....')
#Connecting to the client
conn, addr = s.accept()  
print('Got connection from', addr )  
#Sending a message to the client for announcing that the server is ready
send(conn, "The Server is ready to chat")
#Program's loop
while True:
    #Checking if the command is to exit
	if (msg:=input("Server: ")) != "exit":
		send(conn, msg)
	else:
		s.shutdown(socket.SHUT_RDWR)
		exit()
	#Receiving client's message
	print("Client:", receive(conn))