import threading
import socket
class server_handler(threading.Thread):
	def __init__(self, sock):
		threading.Thread.__init__(self)
		self.clientSock = sock
	def run(self):
		while True:
			data = self.clientSock.recv(1024)
			print data
			self.clientSock.send(data)
			if data == "88":
				break
		self.clientSock.close()
