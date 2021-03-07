#!/usr/bin/env python3

import tkinter as tk
import socket
import threading

class Server():
    server = None
    #HOST_ADDRESS = "71.231.103.175"
    #HOST_ADDRESS = "0.0.0.0"
    #HOST_ADDRESS = socket.gethostname()
    HOST_ADDRESS = "10.0.0.246"
    HOST_PORT = 8080
    client_name = " "
    client_arr = []
    client_name_arr = []

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Wellness Server")

        # Top frame consisting of two buttons widgets (i.e. buttonStart, buttonStop)
        self.topFrame = tk.Frame(self.window)
        self.buttonStart = tk.Button(self.topFrame, text="Connect", command=lambda : self.start_server())
        self.buttonStart.pack(side=tk.LEFT)
        self.buttonStop = tk.Button(self.topFrame, text="Stop", command=lambda : self.stop_server(), state=tk.DISABLED)
        self.buttonStop.pack(side=tk.LEFT)
        self.topFrame.pack(side=tk.TOP, pady=(5, 0))

        # Middle frame consisting of two labels for displaying the host and port info
        self.middleFrame = tk.Frame(self.window)
        self.hostLabel = tk.Label(self.middleFrame, text = "Host: X.X.X.X")
        self.hostLabel.pack(side=tk.LEFT)
        self.portLabel = tk.Label(self.middleFrame, text = "Port:XXXX")
        self.portLabel.pack(side=tk.LEFT)
        self.middleFrame.pack(side=tk.TOP, pady=(5, 0))

        # The client frame shows the client area
        self.clientFrame = tk.Frame(self.window)
        self.labelEntry = tk.Label(self.clientFrame, text="           Client List           ").pack()
        self.scrollBar = tk.Scrollbar(self.clientFrame)
        self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tkDisplay = tk.Text(self.clientFrame, height=15, width=30)
        self.tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
        self.scrollBar.config(command=self.tkDisplay.yview)
        self.tkDisplay.config(yscrollcommand=self.scrollBar.set, background="#F4F6F7", highlightbackground="grey", state="disabled")
        self.clientFrame.pack(side=tk.BOTTOM, pady=(5, 10))

        self.window.mainloop()

    # Start server function
    def start_server(self):
        #global server, HOST_ADDRESS, HOST_PORT # code is fine without this
        self.buttonStart.config(state=tk.DISABLED)
        self.buttonStop.config(state=tk.NORMAL)

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        self.server.bind((self.HOST_ADDRESS, self.HOST_PORT))
        self.server.listen(100)

        threading._start_new_thread(self.accept_clients, (self.server, " "))

        self.hostLabel["text"] = "Host: " + self.HOST_ADDRESS
        self.portLabel["text"] = "Port: " + str(self.HOST_PORT)


    # Stop server function
    def stop_server(self):
        #global server
        self.buttonStart.config(state=tk.NORMAL)
        self.buttonStop.config(state=tk.DISABLED)


    def accept_clients(self, the_server, y):
        while True:
            self.client, self.addr = the_server.accept()
            self.client_arr.append(self.client)
            
            threading._start_new_thread(self.send_receive_client_message, (self.client, self.addr))

    def send_receive_client_message(self, client_connection, client_ip_ADDRESS):
        client_message = " "

        # send welcome message
        self.client_name  = client_connection.recv(4096)
        welcome_str1 = "Welcome! "
        welcome_str1 = str.encode(welcome_str1)
        welcome_str2 = " use 'exit' to quit."
        welcome_str2 = str.encode(welcome_str2)

        client_connection.send(welcome_str1)
        client_connection.send(self.client_name)
        client_connection.send(welcome_str2)

        self.client_name_arr.append(self.client_name)

        self.update_client_names_display(self.client_name_arr)


        while True:
            data = client_connection.recv(4096)
            if not data: break
            if data == "exit": break

            client_message = data

            client_index = self.get_client_index(self.client_arr, client_connection)
            sending_client_name = self.client_name_arr[client_index]

            print("client name: ", type(sending_client_name))
            print("client message: ", type(client_message))
            
            arrow = "->"
            arrow = str.encode(arrow)

            for client in self.client_arr:
                if client != client_connection:
                    client.send(sending_client_name)
                    client.send(arrow)
                    client.send(client_message)

        # find the client index then remove from both lists(client name list and connection list)
        client_index = self.get_client_index(self.client_arr, client_connection)
        del self.client_name_arr[client_index]
        del self.client_arr[client_index]
        client_connection.send("BYE!")
        client_connection.close()

        self.update_client_names_display(self.client_name_arr)  # update client names display


    # Return the index of the current client in the list of clients
    def get_client_index(self, client_list, curr_client):
        client_index = 0
        for conn in client_list:
            if conn == curr_client:
                break
            client_index = client_index + 1

        return client_index


    # Update client name display when a new client connects OR
    # When a connected client disconnects
    def update_client_names_display(self, name_list):
        self.tkDisplay.config(state=tk.NORMAL)
        self.tkDisplay.delete('1.0', tk.END)

        for client in name_list:
            client = client.decode("utf-8")
            client = client + "\n"
            client = str.encode(client)
            self.tkDisplay.insert(tk.END, client)
        self.tkDisplay.config(state=tk.DISABLED)

server = Server()
