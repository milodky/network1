import socket
from time import ctime
import server_handler
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
			print "connected from: ", ClientAddr
			data = clientSock.recv(1024)
			print data
			if data:
				_handler = server_handler.server_handler(clientSock)
				_handler.start()
				_handler.join()
			data = ""
		self.sock.close()
if __name__ == "__main__":
	_server = Server("", 12345)
	_server.server_start()
