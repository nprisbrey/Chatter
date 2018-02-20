import socket
import threading
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#sock.setblocking(0)
print("What ip do you want to connect to?")
ip=raw_input()
print("What port do you want to connect on?")
port=raw_input()
try:
	sock.connect((ip,int(port)))
except socket.error:
	print("Could not connect to the server")
	quit()
clientnum=sock.recv(8)
while len(clientnum) < 4:
	clientnum="0" + clientnum
print("You have joined as Client #" + clientnum + "! Type q and then press 'Enter' to quit.")
def sending():
	while True:
		typed=raw_input()
		if typed != "":
			sock.send(clientnum)
			sock.send(typed)
			if typed == "q":
				break
def recieving():
	while True:
		response=sock.recv(4096)
		if response=="":
			break
		else:
			print(response)
	sock.close()
t1=threading.Thread(target=sending)
t2=threading.Thread(target=recieving)
t1.daemon=True
t2.daemon=True
t1.start()
t2.start()
t1.join()
t2.join()
