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
		conn.send(b"%%EMT%%%%END%%")
	else:
		#Encoding the text into binary
		result = txt.encode()
		#Splitting the encoded text into smaller packets to send if needed so we can send texts with any size
		result = [result[group*1017:(group+1)*1017] for group in range(int(len(result)/1017 if len(result)%1017 == 0 else len(result)//1017+1))]
		#1024 - 7 => packet size - end phrase length
		result[len(result)-1] = result[len(result)-1] + "%%END%%".encode()
		for packet in result:
			# Send the message to the client
			conn.send(packet)
			while True:
				if (n:=conn.recv(1024)) == b"%%ACK%%":
					break

#Socket object
client = socket.socket()
#Connecting to the server
client.connect((socket.gethostname(), 60417))
print(receive(client))
while True:
	#Receiving Server's message
	print("Server:", receive(client))
    #Checking if the command is to exit
	if (msg:=input("Client: ")) != "exit":
		send(client, msg)
	else:
		exit()