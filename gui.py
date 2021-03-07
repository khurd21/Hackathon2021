#!/usr/bin/env python3

import tkinter as tk
from custom_client import Client
from profile import Profile
import glob

class GUI:
    def __init__(self, master=None):
        # Profile() class
        print(glob.profileList)
        # The typical stuff
        self.master = master
       
        self.btn_monitor = 0

        # Button and Setting Location 
        self.btn_refresh = tk.Button(self.master, text='Toggle', command=self.button_refresh_clicked)
        self.btn_start_chat = tk.Button(self.master, text='Start Chat', command=self.button_start_chat_clicked)

        self.btn_refresh.place(relx=0.7, rely=0.9,anchor=tk.CENTER)
        self.btn_start_chat.place(relx=0.3, rely=0.9,anchor=tk.CENTER)

        # Labels and Setting Location
        self.user_title = tk.Label(self.master, text='Wellness Chat')
        self.user_title.config(font=("Courier",35))
        self.user_label = tk.Label(self.master, text=f'Welcome to wellness chat, {glob.user_profile.name}! Please click the buttons\n' \
                                                    'below to view friends online\n or load up the chat window.')
        self.label = tk.Label(self.master, text='')

        self.user_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        self.user_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.label.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        # settings
        self.popupLabel = tk.Label(self.master, text="Color Settings")
        self.popupLabel.pack(side=tk.BOTTOM)

        self.popupMenu = tk.Menu(self.master, tearoff=0)

        self.popupMenu.add_command(label = "Red", command = lambda : self.settings("Red"))
        self.master.bind("<Button-3>", self.popup)

        self.popupMenu.add_command(label = "Green", command = lambda : self.settings("Green"))
        self.master.bind("<Button-3>", self.popup)

        self.popupMenu.add_command(label = "Pink", command = lambda : self.settings("Pink"))
        self.master.bind("<Button-3>", self.popup)

        self.popupMenu.add_command(label = "Gray", command = lambda : self.settings("Gray"))
        self.master.bind("<Button-3>", self.popup)

        self.popupMenu.add_command(label = "Purple", command = lambda : self.settings("Purple"))
        self.master.bind("<Button-3>", self.popup)

        self.popupMenu.add_command(label = "Blue", command = lambda : self.settings("Blue"))
        self.master.bind("<Button-3>", self.popup)

        self.popupMenu.add_command(label = "Yellow", command = lambda : self.settings("Yellow"))
        self.master.bind("<Button-3>", self.popup)

        self.popupMenu.add_command(label = "Light Mode", command = lambda : self.settings("White"))
        self.master.bind("<Button-3>", self.popup)

        self.popupMenu.add_command(label = "Dark Mode", command = lambda : self.settings("#19201B"))
        self.master.bind("<Button-3>", self.popup)
        return

    def popup(self, event):
        try:
            self.popupMenu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popupMenu.grab_release()

    def settings(self, message):
        self.master.configure(background=message)

    def button_refresh_clicked(self):
        print('Refresh Button Clicked')

        # Monitor How Many Times Button Pressed
        self.btn_monitor += 1
        self.btn_monitor = self.btn_monitor % 2
        if self.btn_monitor == 1:
            self.user_title.config(text='Members Online')
            self.label.config(text=f'Greetings, {glob.user_profile.name}')
            string = ''
            for i, fr in enumerate(glob.profileList):
                if i % 3 == 0:
                    string += '\n'
                string += f'*** {fr.name} ***'

            self.user_label.config(text=string)
            self.user_label.place(relx=0.5,rely=0.2,anchor=tk.CENTER)

        else:
            self.user_title.config(text='Wellness Chat')
            self.user_label.config(text=f'Welcome to Wellness Chat, {glob.user_profile.name}!\nPlease click the buttons' \
                                        'below to view friends online or\nload up the chat window.')
            self.user_label.place(relx=0.5,rely=0.3,anchor=tk.CENTER)
            self.label.config(text='')
        return


    def button_start_chat_clicked(self):
        print('Start Chat Button Clicked')
        self.client = Client("rgusa")
        return
