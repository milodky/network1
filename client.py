import socket
import sender
import receiver
from time import ctime

class client:
	def __init__(self, ServerIP, ServerPort):
		self.ServerAddr = (ServerIP, ServerPort)
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect(self.ServerAddr)
		self.Receiver = receiver.receiver(self.sock)
		self.Sender = sender.sender(self.sock)
		#self.lock = 
	def send_msg(self):
		self.Sender.start()
		self.Receiver.start()
		self.Receiver.join()
		self.Sender.join()
		print "See you!"
		self.sock.close()
	"""
		while True:
			data = raw_input('> ')
			self.sock.send(data)
			if data == '88':
				break
			data = self.sock.recv(1024)
			print data
		self.sock.close()
	"""
if __name__ == "__main__":
	_client = client("127.0.0.1", 11115)
	_client.send_msg()
