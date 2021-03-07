#!/usr/bin/env python3

import tkinter as tk
from profile import Profile
from functools import partial

class GUI:
    def __init__(self, master=None, profile=None):
        # Profile() class
        self.profile = profile

        # The typical stuff
        self.master = master

        # Btn and txt
        self.btn = tk.Button(self.master, text='Click Me!', command=self.button_clicked)
        self.btn.place(relx=0.5, rely=0.9,anchor=tk.CENTER)
        self.label = tk.Label(self.master, text='')
        self.label.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        return

    def button_clicked(self):
        print(f'Hello, {self.profile.name}')
        self.label.config(text=f'Greetings, {self.profile.name}')
        return

def main():
    window = tk.Tk()
    window.geometry('600x800')
    window.title('Wellness Chat')
    frame = tk.Frame(window)

    profile = Profile()
    profile.name = "Silas :("
    gui = GUI(window, profile)
    gui.master.mainloop()
    return



if __name__ == '__main__':
    main()
