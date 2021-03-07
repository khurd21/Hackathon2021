#!/usr/bin/env python3

import tkinter as tk
from profile import Profile
from functools import partial

class GUI:
    def __init__(self, master=None, profile=None, friends=None):
        # Profile() class
        self.profile = profile
        self.friends = friends

        # The typical stuff
        self.master = master

        # Btn and txt
        self.btn_refresh = tk.Button(self.master, text='Refresh', command=self.button_refresh_clicked)
        self.btn_start_chat = tk.Button(self.master, text='Start Chat', command=self.button_start_chat_clicked)

        self.btn_refresh.place(relx=0.5, rely=0.9,anchor=tk.CENTER)
        self.btn_start_chat.place(relx=0.4, rely=0.9,anchor=tk.CENTER)

        self.label = tk.Label(self.master, text='')
        self.label.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        return

    def button_refresh_clicked(self):
        print('Refresh Button Clicked')
        self.label.config(text=f'Greetings, {self.profile.name}')
        return

    def button_start_chat_clicked(self):
        print('Start Chat Button Clicked')
        self.label.config(text=f'This would be the chat window.')
        return

STATE = 0

def display_menu():
    window = tk.Tk()
    window.geometry('600x800')
    window.title('Wellness Chat')
    frame = tk.Frame(window)

    profile_list = []
    profile = Profile()

    profile.name = "Silas :("
    profile.mood = 4
    profile.avatar = None
    profile.contact = True
    profile.id = 1234
    profile_list.append(profile)
    
    profile.name = "Kyle"
    profile.mood = 6
    profile.avatar = None
    profile.contact = True
    profile.id = 54321
    profile_list.append(profile)

    current_user = Profile()
    current_user.name = 'Riley'
    current_user.mood = 10
    current_user.avatar = None
    current_user.contact = True
    current_user.id = 69420
    
    gui = GUI(window, current_user, profile_list)
    gui.master.mainloop()
    STATE = 1
    return


def main():
    global STATE
    while True:
        if STATE == 0:
            display_menu()
        elif STATE == 1:
            print('Please work!')
            STATE = 0
    return



if __name__ == '__main__':
    main()
