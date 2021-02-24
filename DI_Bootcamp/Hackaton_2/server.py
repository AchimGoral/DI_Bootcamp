import socket
import sqlite3 as sl
import database_chat as dbc

# IP_SERVER = '192.168.1.42'


class Server:

	def __init__(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((socket.gethostname(),1234))
		s.listen(5)
		while True:
			self.clientsocket, address = s.accept()
			print(f"Connection from {address} has been established!")
			self.listen_message()

	# def storing message

	def check_user(self,username):
		pass
		#select query to db
		#check if the username exists and unique
		#if username doesn't exist in the db:
			# return '51'
		#elif username exists :
			#return '50'
		
	def check_connection(self, receiver):
		pass
		#check if to user is connected
		#if not send a 55 failed message user not available
		#if socket connected send a 54 success message


	def listen_message(self):
		data_from_client = self.clientsocket.recv(1024)
		data_from_client = data_from_client.decode()
		data_chopped = data_from_client.split(',')

		print(data_chopped)

		if data_chopped[0] == 'snd':
			self.send_message(data_chopped[1], data_chopped[2]) #[1]=msg, [2]=receiver
		elif data_chopped[0] == 'sup':
			self.signup_server(data_chopped[1], data_chopped[2]) #[1]=username, [2]=IP
		elif data_chopped[0] == 'sig':
			self.signin_server(data_chopped[1]) #[1]=username
		else:
			print("Error")
		# if	data_chopped[0] == 'snd':
		# 	self.send_message(data_chopped[1], data_chopped[2])
		# elif data_chopped[0] in ('sup', 'sig'):
		# 	res = self.check_user(data_chopped)
		# 	if res == '50':
		# 		self.clientsocket.send(bytes("50", "utf-8"))
		# 	elif res == '51':
		# 		self.clientsocket.send(bytes("51", "utf-8"))
		# else:
		# 	res = self.check_connection(data_chopped)
		# 	if res == '54':
		# 		self.clientsocket.send(bytes("54", "utf-8"))
		# 	elif res == '55':
		# 		self.clientsocket.send(bytes("55", "utf-8"))

	def send_message(self, message, receiver):
		print(f"send message {message} {receiver}")
		#select the right socket from the db 
		#send the message to the right socket

	def signup_server(self, username, ip_address):
		dbc.signup_server_db(username, ip_address)

	def signin_server(self, username):
		dbc.signin_server_db(username)

	# def close server