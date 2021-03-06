#!/usr/bin/env python3

import tkinter as tk
import socket
import threading

# use: "variable name" = Client() and it will construct client

class Client:
    client = None
    HOST_ADDR = "0.0.0.0"
    HOST_PORT = 8080

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Custom Client")
        self.username = " "

        self.topFrame = tk.Frame(self.window)
        self.lblName = tk.Label(self.topFrame, text = "Name:").pack(side=tk.LEFT)
        self.entryName = tk.Entry(self.topFrame)
        self.entryName.pack(side=tk.LEFT)
        self.buttonConnect = tk.Button(self.topFrame, text="Connect", command=lambda : self.connect())
        self.buttonConnect.pack(side=tk.LEFT)
        self.topFrame.pack(side=tk.TOP)

        self.displayFrame = tk.Frame(self.window)
        self.lblLine = tk.Label(self.displayFrame, text="*********************************************************************").pack()
        self.scrollBar = tk.Scrollbar(self.displayFrame)
        self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tkDisplay = tk.Text(self.displayFrame, height=20, width=55)
        self.tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
        self.tkDisplay.tag_config("tag_your_message", foreground="blue")
        self.scrollBar.config(command=self.tkDisplay.yview)
        self.tkDisplay.config(yscrollcommand=self.scrollBar.set, background="#F4F6F7", highlightbackground="grey", state="disabled")
        self.displayFrame.pack(side=tk.TOP)

        self.bottomFrame = tk.Frame(self.window)
        self.tkMessage = tk.Text(self.bottomFrame, height=2, width=55)
        self.tkMessage.pack(side=tk.LEFT, padx=(5, 13), pady=(5, 10))
        self.tkMessage.config(highlightbackground="grey", state="disabled")
        self.tkMessage.bind("<Return>", (lambda event: self.getChatMessage(self.tkMessage.get("1.0", tk.END))))
        self.bottomFrame.pack(side=tk.BOTTOM)

        self.window.mainloop()
    
    # network client
    def connect(self):
        #global username, client
        if len(self.entryName.get()) < 1:
            tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter your first name <e.g. John>")
        else:
            self.username = self.entryName.get()
            self.connect_to_server(self.username)



    def connect_to_server(self, name):
        #global client, HOST_PORT, HOST_ADDR
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.HOST_ADDR, self.HOST_PORT))
            self.client.send(name) # Send name to server after connecting

            self.entryName.config(state=tk.DISABLED)
            self.buttonConnect.config(state=tk.DISABLED)
            self.tkMessage.config(state=tk.NORMAL)

            # start a thread to keep receiving message from server
            # do not block the main thread :)
            threading._start_new_thread(self.receive_message_from_server, (self.client, "m"))
        except Exception as e:
            tk.messagebox.showerror(title="ERROR!!!", message="Cannot connect to host: " + self.HOST_ADDR + " on port: " + str(self.HOST_PORT) + " Server may be Unavailable. Try again later")


    def receive_message_from_server(self, sck, m):
        while True:
            from_server = sck.recv(4096)

            if not from_server: break

            # display message from server on the chat window

            # enable the display area and insert the text and then disable.
            # why? Apparently, tkinter does not allow us insert into a disabled Text widget :(
            texts = self.tkDisplay.get("1.0", tk.END).strip()
            self.tkDisplay.config(state=tk.NORMAL)
            if len(texts) < 1:
                self.tkDisplay.insert(tk.END, from_server)
            else:
                self.tkDisplay.insert(tk.END, "\n\n"+ from_server)

            self.tkDisplay.config(state=tk.DISABLED)
            self.tkDisplay.see(tk.END)

        sck.close()
        self.window.destroy()


    def getChatMessage(self, message):

        message = message.replace('\n', '')
        texts = self.tkDisplay.get("1.0", tk.END).strip()

        # enable the display area and insert the text and then disable.
        # why? Apparently, tkinter does not allow use insert into a disabled Text widget :(
        self.tkDisplay.config(state=tk.NORMAL)
        if len(texts) < 1:
            self.tkDisplay.insert(tk.END, "You->" + message, "tag_your_message") # no line
        else:
            self.tkDisplay.insert(tk.END, "\n\n" + "You->" + message, "tag_your_message")

        self.tkDisplay.config(state=tk.DISABLED)

        self.send_mssage_to_server(message)

        self.tkDisplay.see(tk.END)
        self.tkMessage.delete('1.0', tk.END)


    def send_mssage_to_server(self, message):
        self.client.send(message)
        if message == "exit":
            self.client.close()
            self.window.destroy()
        print("Sending message")

client = Client()
