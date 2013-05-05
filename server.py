import socket
from time import ctime
class Server:
	def __init__(self, myIP, myPort):
		self.addr = (myIP, myPort)
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind(self.addr)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.listen(5)

	def server_start(self):
		while True:
			clientSock, ClientAddr = self.sock.accept()
			print 'connetcted from: ', ClientAddr
			while True:
				data = clientSock.recv(1024)
				print data
				if data == "88":
					break
				clientSock.send('aaa')
		self.sock.close()
		clientSock.close()
if __name__ == "__main__":
	_server = Server("", 1234)
	_server.server_start()
