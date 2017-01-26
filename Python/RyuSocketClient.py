from PyQt5 import QtCore
import socket, _thread, time


class RyuSocketClient:

	def __init__(self):
		self.OnReceived = None

		self.que = []
		self.lock_ = _thread.allocate_lock()
		self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.on_timer)
		self.timer.start(50)

	def connect(self, host, port):
		self.lock_.acquire()
		try:
			self.socket_.connect( (host, port) )
			self.thread_ = _thread.start_new_thread( self.on_thread_run, ("thread", ) )
		finally:
			self.lock_.release()

	def send(self, text):
		self.lock_.acquire()
		try:
			self.socket_.send( text.encode() )
		finally:
			self.lock_.release()

	def getMsg(self):
		self.lock_.acquire()
		try:
			if len(self.que) > 0:
				return self.que.pop()
			else:
				return ""
		finally:
			self.lock_.release()

	def setOnReceived(self, event_handler):
		self.OnReceived = event_handler

	def on_thread_run(self, arg_01):
		while True:
			line = self.socket_.recv(2048)

			self.lock_.acquire()
			try:
				self.que.append( line.decode() )
			finally:
				self.lock_.release()

	def on_timer(self):
		line = self.getMsg()
		if (line != "") and (self.OnReceived != None):
		    self.OnReceived(line)
