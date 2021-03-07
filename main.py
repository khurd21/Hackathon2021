#!/usr/bin/env python3

import glob
from profile import Profile
from profile import Friend
import tkinter as tk
import login_screen
import gui


def display_menu():
    window = tk.Tk()
    window.geometry('600x350')
    window.title('Wellness Chat')
    frame = tk.Frame(window)
    
    g = gui.GUI(window)
    g.master.mainloop()
    return


def main():

    login_screen.readcsv()
    login_screen.printProfiles()
    login_screen.save_users()
    gui = login_screen.LoginScreen()
    gui.loginScreen()
    gui.window.mainloop()
    display_menu()
    return

if __name__ == '__main__':
    main()
