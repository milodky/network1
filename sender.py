import threading
import socket

class sender(threading.Thread):
	def __init__(self, sock):
		threading.Thread.__init__(self)
		self.sock = sock
	def run(self):
		print "abcd"
		while True:
			data = raw_input('')
			self.sock.send(data)
			if data == '88':
				break
