import socket
from time import ctime

class client:
	def __init__(self, ServerIP, ServerPort):
		self.ServerAddr = (ServerIP, ServerPort)
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect(self.ServerAddr)

	def send_msg(self):
		while True:
			data = raw_input('> ')
			self.sock.send(data)
			if data == '88':
				break
			data = self.sock.recv(1024)
			print data
		self.sock.close()

if __name__ == "__main__":
	ye = client("127.0.0.1", 1234)
	ye.send_msg()
