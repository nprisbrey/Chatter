import socket
import select
import time
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("What port would you like to host on?")
servport=input()
sock.bind(("127.0.0.1",servport))
sock.listen(1)
sock.setblocking(0)
pr=[]
pw=[]
pe=[]
rtr=[]
rtw=[]
ie=[]
words=[]
while(True):
	try:
		(client,(ip,port))=sock.accept()
		client.setblocking(0)
		pr.append(client)
		pw.append(client)
		client.send(str(len(pw)))
		words.append("Client #" + str(len(pw)) + " has joined.")
		print("Client #" + str(len(pw)) + " has joined.")
	except socket.error:
		print("No additional clients...")
	print(rtr)
	print(rtw)
	print(ie)
	rtr, rtw, ie = select.select(pr, pw, pe, 1)
	for cl in rtr:
		#try:
		clientnum=cl.recv(4)
		response=cl.recv(4096)
		if response == "q":
			words.append("Client #" + clientnum + " has left.")
			print("Client #" + clientnum + " has left.")
			pr.remove(cl)
			pw.remove(cl)
			cl.send("Thanks for joining!!!")
			cl.close()
		else:
			words.append("Client #" + clientnum + ": " + response)
		print("Client #" + clientnum + ": " + response)
		#except socket.error:
			#print("What is happening?")		
	for cl in rtw:
		for word in words:
			try:
				cl.send(word)
			except socket.error:
				print("Had a problem sending a message to a client.")
	words=[]
	time.sleep(1)
