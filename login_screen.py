#!/usr/bin/python

#import tkinter as tk
#import profile
from tkinter import *
from functools import partial
#top = Tkinter.Tk()

def validateLogin(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())
    return
class GUI:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Wellness Check")
        self.topFrame = Frame(self.window)
        
        # Code to add widgets will go here...
        #import Toplevel
        #import panedWindow to set up windows
            # left is the free world for the friend net. 
            # right up is menu bar
            # right low is friend list/add friend
        #import tkMessageBox for mood 
        #self = window.mainloop()
    

    def loginScreen(self):
        print("login screen")
        #username label and text entry box
        usernameLabel = Label(self.window, text="User Name").grid(row=0, column=0)
        username = StringVar()
        usernameEntry = Entry(self.window, textvariable=username).grid(row=0, column=1)  
        passwordLabel = Label(self.window,text="Password").grid(row=1, column=0)  
        password = StringVar()
        passwordEntry = Entry(self.window, textvariable=password, show='*').grid(row=1, column=1)  
        validatelogin = partial(validateLogin, username, password)
        loginButton = Button(self.window, text="Login", command=validatelogin).grid(row=4, column=0)  


gui = GUI()
gui.loginScreen()
gui.window.mainloop()