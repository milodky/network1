import threading
import socket
class server_handler(threading.Thread):
	user = {}
	item = []
	cnt = 0
	def __init__(self, sock):
		threading.Thread.__init__(self)
		self.clientSock = sock
		self.login = 0
		self.name = ""
	def run(self):
		while True:
			rdata = self.clientSock.recv(1024)
			print rdata
			data_info = rdata.split(' ')
			data = ""
			if (not cmp(data_info[0].lower(), 'login')):
				if (self.login == 0):
					self.login = 1
					addr = self.clientSock.getpeername()
					self.name = data_info[1].lower()
					print addr
					server_handler.user[self.name] = addr
					data = "Registered!"
				else:
					data = "Already Online!"
			elif (not cmp(data_info[0].lower(), 'bid')):
				_item = {}
				description = ""
				for j in range(3, len(data_info)):
					print data_info[j]
					description = description + data_info[j] + " "
				_item["number"] = str(server_handler.cnt)
				_item["itemname"] = data_info[0]
				_item["price"] = data_info[1]
				_item["description"] = description
				_item["username"] = self.name
				server_handler.item.append(_item)
				data = "Bid handled!"
				server_handler.cnt += 1
			elif (not cmp(data_info[0].lower(), 'show')):
				if (not server_handler.item):
					data = "No items found!"
				else:
					for elem in server_handler.item:
						data = data + elem["number"]
						data = data + " " + elem["username"]
						data = data + " " + elem["itemname"]
						data = data + " " + elem["price"]
						data = data + " " + elem["description"]
						data = data + '\n'
			elif (rdata == "88"):
				self.clientSock.send("88")
				break
			self.clientSock.send(data)
		self.clientSock.close()
