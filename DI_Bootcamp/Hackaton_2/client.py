import socket
import tkinter as tk

# IP_SERVER = '192.168.1.42'

# WIDTH = 300
# HEIGHT = 300

class Client:

	def __init__(self):
		self.hostname = socket.gethostname()
		self.ip_address = socket.gethostbyname(self.hostname)

	# def tk_login(self):

	# 	root = tk.Tk()

	# 	canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
	# 	canvas.pack()

	# 	frame = tk.Frame(root, bg='#80c1ff', bd=5)
	# 	frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

	# 	button = tk.Button(frame, text="Sign In", font=25)#, command=lambda: get_weather(entry.get()))
	# 	button.place(relx=0, relheight=1, relwidth=0.5)

	# 	button = tk.Button(frame, text="Sign Up", font=25)#, command=lambda: get_weather(entry.get()))
	# 	button.place(relx=0.5, relheight=1, relwidth=0.5)

	# 	lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
	# 	lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

	# 	entry1 = tk.Entry(lower_frame, font=40)
	# 	entry1.insert(0, 'Username')
	# 	entry1.place(relwidth=1, relheight=0.2)

	# 	entry2 = tk.Entry(lower_frame, font=40)
	# 	entry2.insert(0, 'IP')
	# 	entry2.place(rely=0.25,relwidth=1, relheight=0.2)


	# 	root.mainloop()

	# def tk_text():

	# 	root = tk.Tk()

	# 	canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
	# 	canvas.pack()

	# 	frame = tk.Frame(root, bg='#80c1ff', bd=5)
	# 	frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

	# 	entry = tk.Entry(frame, font=40)
	# 	entry.insert(0, 'Your text here')
	# 	entry.place(relwidth=0.49, relheight=1)

	# 	button = tk.Button(frame, text="Send", font=25)#, command=lambda: get_weather(entry.get()))
	# 	button.place(relx=0.75, relheight=1, relwidth=0.25)

	# 	button = tk.Button(frame, text="Delete", font=25)#, command=lambda: get_weather(entry.get()))
	# 	button.place(relx=0.5, relheight=1, relwidth=0.25)

	# 	lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
	# 	lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

	# 	label = tk.Label(lower_frame)
	# 	label.place(relwidth=1, relheight=1)

	# 	root.mainloop()

	def signup(self, username):
		if username:
			username = f'sup,{username},{self.ip_address}'
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((socket.gethostname(), 1234)) # Hardcode IP-Address for server
			s.send(username.encode())

	def signin(self, username):
		if username:
			username = f'sig,{username},{self.ip_address}'
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((socket.gethostname(), 1234)) # Hardcode IP-Address for server
			s.send(username.encode())

	def send(self, message, receiver):
		if message:
			message = f'snd,{message},{receiver}'
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((socket.gethostname(), 1234)) # Hardcode IP-Address for server
			s.send(message.encode())
			message_recv = s.recv(1024)
			print(message_recv.decode("utf-8"))
		# take a message
		# send to the server
		# display all the history

	def listen_message(self):
		data_from_server = self.serversocket.recv(1024)
		data_from_server = data_from_server.decode()

		if	data_from_server == '50':
			pass
			#open tkinter Connection window asking for a "to username"
		elif data_from_server == '51':
			pass
			#open tkinter Registration window asking for a "signup username"
		elif data_from_server == '54':
			pass
			#if first time after registration or signin
			#display a success message
			#open tkinter Connection window asking for a receiver
			#if not first time:
			#open chat window and start to send message
		elif data_from_server == '55':
			pass
			#connection with the receiver failed. he is not available


	def open_window(self):
		pass
		#only open the right window of chat 
		#registration OR Connection OR chat 

	# def delete message
	#     ask the server for deleting

	# def close socket

	# def display message