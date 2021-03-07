#!/usr/bin/python

import tkinter as tk
import glob
import csv
import json
import sys
from profile import Friend 
from profile import Profile
from functools import partial
from time import sleep
from create_account import CreateAccount
def save_users():
    with open('data/users_test.csv', 'w') as f:
        for i in glob.profileList:
            print("printing to outfile")
            i.save_user_data(f)
    f.close()


def getLength():
    with open('data/users.csv','|', newline='') as f:
        return sum(1 for line in f)


def printProfiles():
    for p in glob.profileList:
        print(p.name)


#Silas|10|None|1|{'Kyle':12,'Riley':15}|12345|hellamegaawesome|
#Kyle|3|None|0|None|1234|asdasdasdasd|
#Riley|10|None|0|None|123|pw|
#name, mood, avatar, contact, friendsList, id,password,
def readcsv():
    print("in read csv")
    with open('data/users.csv', newline='') as f:
        reader = csv.reader(f, delimiter='|')

        for row in reader:
            print(f"Name: {row[0]}")
            friend_list = []
            p = Profile()
            p.name = row[0]
            p.mood = int(row[1])
            p.avatar = row[2]
            p.contact = int(row[3])
            #FRIENDS
            if row[4] == "[None]":
                js = None
                friend_list = None
            else: 
                #js = json.loads(row[4])
                js = eval(row[4])
                for j in js:
                    print(j)
                    fr = Friend()
                    fr.root = row[0]
                    fr.friend = j['Name']
                    print(f"In j and the dict value for name is: {fr.friend}")
                    fr.dateToContact = j['dateToContact']
                    fr.wellnessCheckFrequency = j['Name']
                    friend_list.append(fr)
            p.friendsList = friend_list
            p.id = row[5]
            p.password = row[6]
            glob.profileList.append(p)
            #json.dump(p,sys.stdout)
    print("printing profile List")
    return


class LoginScreen:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Wellness Check")
        self.window.geometry("300x150")
        self.topFrame = tk.Frame(self.window)
        self.is_correct_text = tk.Label(self.window,text='')
        self.is_correct_text.place(relx=0.5,rely=0.9,anchor=tk.CENTER)

    def validateLogin(self,username, password):
        for p in glob.profileList:
            if (username.get() == p.name and password.get() == p.password):
                glob.user_profile = p
                self.is_correct_text.config(text=f'Correct! Welcome, {p.name}')
                print("matched!")
                sleep(2)
                self.window.destroy()
                return True
        print("wrong username or password")
        self.is_correct_text.config(text='Incorrect!')
        return

    def deiconify(self):
        self.window.deiconify()

    def createProfileWindow(self):
       # self.window.withdraw()
        self.window.destroy()
        gui = CreateAccount(glob.profileList, glob.user_profile)
        gui.displayScreen()
        gui.window.mainloop()
        #gui.window.destroy()

    def loginScreen(self):
        print("login screen")
        usernameLabel = tk.Label(self.window, text="User Name").grid(row=0, column=0)
        username = tk.StringVar()
        usernameEntry = tk.Entry(self.window, textvariable=username).grid(row=0, column=1)  
        passwordLabel = tk.Label(self.window,text="Password").grid(row=1, column=0)  
        password = tk.StringVar()
        passwordEntry = tk.Entry(self.window, textvariable=password, show='*').grid(row=1, column=1)  
        validatelogin = partial(self.validateLogin, username, password)
        loginButton = tk.Button(self.window, text="Login", command=validatelogin).grid(row=4, column=1)  

        createProfileFunc = partial(self.createProfileWindow)
        createAccountBtn = tk.Button(self.window, text = "Create Account", command=createProfileFunc).grid(row = 4, column = 0)
