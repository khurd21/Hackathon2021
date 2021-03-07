#!/usr/bin/env python3

import tkinter as tk
import socket
import threading
import pygame

# use: "variable name" = Client() and it will construct client

class Client:
    client = None
    HOST_ADDR = "10.0.0.246"
    #HOST_ADDR = "71.231.103.175"
    #HOST_ADDR = socket.gethostname()
    #HOST_ADDR = "0.0.0.0"
    HOST_PORT = 8080

    def __init__(self, name):
        # pygame.mixer.init()

        self.window = tk.Tk()
        self.window.title("Wellness Client")
        self.username = name

        self.topFrame = tk.Frame(self.window)
        self.topFrame.pack(side=tk.TOP)

        self.bottomFrame = tk.Frame(self.window)

        self.popupLabel = tk.Label(self.bottomFrame, text="Sounds to send", background="pink")
        self.popupLabel.pack(side=tk.RIGHT)

        self.popupMenu = tk.Menu(self.bottomFrame, tearoff=0)
        self.popupMenu.add_command(label = "Bruh!", command = lambda : self.playSounds("Bruh!"))
        self.bottomFrame.bind("<Button-3>", self.popup)
        self.popupMenu.add_command(label = "Nani!", command = lambda : self.playSounds("Nani!"))
        self.bottomFrame.bind("<Button-3>", self.popup)
        self.popupMenu.add_command(label = "Do it!", command = lambda : self.playSounds("Do it!"))
        self.bottomFrame.bind("<Button-3>", self.popup)
        self.popupMenu.add_command(label = "Yeah!", command = lambda : self.playSounds("Yeah!"))
        self.bottomFrame.bind("<Button-3>", self.popup)
        self.popupMenu.add_command(label = "Wow", command = lambda : self.playSounds("Wow"))
        self.bottomFrame.bind("<Button-3>", self.popup)
        self.popupMenu.add_command(label = "I am groot.", command = lambda : self.playSounds("I am groot."))
        self.bottomFrame.bind("<Button-3>", self.popup)
        self.popupMenu.add_command(label = "Bazinga!", command = lambda : self.playSounds("Bazinga!"))
        self.bottomFrame.bind("<Button-3>", self.popup)
        self.popupMenu.add_command(label = "Windows OS", command = lambda : self.playSounds("Windows OS"))
        self.bottomFrame.bind("<Button-3>", self.popup)
        self.popupMenu.add_command(label = "WilHelm Scream", command = lambda : self.playSounds("sounds/WilHelm Scream"))
        self.bottomFrame.bind("<Button-3>", self.popup)
        
        self.tkMessage = tk.Text(self.bottomFrame, height=1, width=55)
        self.tkMessage.pack(side=tk.LEFT, padx=(5, 13), pady=(5, 10))
        self.tkMessage.config(highlightbackground="grey", state="disabled")
        self.tkMessage.bind("<Return>", (lambda event: self.receive_message_from_chat(self.tkMessage.get("1.0", tk.END))))
        self.bottomFrame.pack(side=tk.BOTTOM)

        self.displayFrame = tk.Frame(self.window)
        self.scrollBar = tk.Scrollbar(self.displayFrame)
        self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tkDisplay = tk.Text(self.displayFrame, height=20, width=55)
        self.tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
        self.tkDisplay.tag_config("tag_your_message", foreground="purple")
        self.scrollBar.config(command=self.tkDisplay.yview)
        self.tkDisplay.config(yscrollcommand=self.scrollBar.set, background="#F4F6F7", highlightbackground="grey", state="disabled")
        self.displayFrame.pack(side=tk.TOP)

        self.connect_client2server()

        self.window.mainloop()

    def connect_client2server(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            self.client.connect((self.HOST_ADDR, self.HOST_PORT))
            self.client.send(str.encode(self.username))

            self.tkMessage.config(state=tk.NORMAL)

            threading._start_new_thread(self.receive_message_from_server, (self.client, "m"))
        except Exception as e:
            print("Exception thrown (connect_client2server): ")
            print(e)

    def receive_message_from_server(self, sck, arb):
        while True:
            from_server = sck.recv(4096)
            from_server = from_server.decode("utf-8")

            if not from_server: break

            texts = self.tkDisplay.get("1.0", tk.END).strip()
            self.tkDisplay.config(state=tk.NORMAL)
            if len(texts) < 1:
                self.tkDisplay.insert(tk.END, from_server)
            else:
<<<<<<< HEAD
                self.tkDisplay.insert(tk.END,'\n'+ from_server)
=======
                self.tkDisplay.insert(tk.END, "\n"+ from_server)
>>>>>>> d1f54a8208fe4e7c69ecb78bbfb120ae049b8ea7

            self.tkDisplay.config(state=tk.DISABLED)
            self.tkDisplay.see(tk.END)

        sck.close()
        self.window.destroy()

    def receive_message_from_chat(self, message):
        print("type: ", type(message))
        message = message.replace('\n', '')
        texts = self.tkDisplay.get("1.0", tk.END).strip()

        self.tkDisplay.config(state=tk.NORMAL)
        if len(texts) < 1:
            self.tkDisplay.insert(tk.END, "You->" + message, "tag_your_message")
        else:
            self.tkDisplay.insert(tk.END, "\n" + "You->" + message, "tag_your_message")

        self.tkDisplay.config(state=tk.DISABLED)

        print(message)
        if message == "Bruh!":
            pygame.mixer.music.load("sounds/movie_1.ogg")
            pygame.mixer.music.play(loops=0)

        elif message == "Nani!":
            pygame.mixer.music.load("sounds/nani.ogg")
            pygame.mixer.music.play(loops=0)

        elif message == "Yeah!":
            pygame.mixer.music.load("sounds/yeah.ogg")
            pygame.mixer.music.play(loops=0)

        elif message == "Wow":
            pygame.mixer.music.load("sounds/wow.ogg")
            pygame.mixer.music.play(loops=0)

        elif message == "Do it!":
            pygame.mixer.music.load("sounds/doit.ogg")
            pygame.mixer.music.play(loops=0)

        elif message == "I am groot.":
            pygame.mixer.music.load("sounds/iamgroot.ogg")
            pygame.mixer.music.play(loops=0)

        elif message == "Bazinga!":
            pygame.mixer.music.load("sounds/bazinga.ogg")
            pygame.mixer.music.play(loops=0)
        
        elif message == "Windows OS":
            pygame.mixer.music.load("sounds/nuclear-fart.ogg")
            pygame.mixer.music.play(loops=0)

        elif message == "WilHelm Scream":
            pygame.mixer.music.load("sounds/wilhelmscream.ogg")
            pygame.mixer.music.play(loops=0)

        self.send_message_to_server(message)
        self.tkDisplay.see(tk.END)
        self.tkMessage.delete('1.0', tk.END)

    def send_message_to_server(self, message):
        self.client.send(str.encode(message))
        if message == "exit":
            self.client.close()
            self.window.destroy()
        print("Sending message")
    
    def bruh(self):
        self.receive_message_from_chat("Bruh!")

    def popup(self, event):
        try:
            self.popupMenu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popupMenu.grab_release()
    
    def playSounds(self, message):
        self.receive_message_from_chat(message)

#client = Client("rgusa")
