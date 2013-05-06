import socket
import threading

class receiver(threading.Thread):
	def __init__(self, sock):
		threading.Thread.__init__(self)
		self.data = ""
		self.sock = sock
	def run(self):
		while True:
			data = self.sock.recv(1024)
			print data
			if data == "88":
				break
