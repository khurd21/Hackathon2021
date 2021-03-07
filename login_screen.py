#!/usr/bin/python

import tkinter as tk
import csv
from profile import Friend 
from profile import Profile
from functools import partial

def getLength():
    with open('data/users.csv', newline='') as f:
        return sum(1 for line in f)
def printProfiles():
    global profileList
    for p in profileList:
        print(p.name)

#name, mood, avatar, contact, friendsList, id,password,
def readcsv():
    global profileList
    print("in read csv")
    with open('data/users.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            friend_list = []
            fr = Friend()
            p = Profile()
            p.name = row[0]
            p.mood = int(row[1])
            p.avatar = row[2]
            p.contact = int(row[3])
            #FRIENDS
            p.id = row[5]
            p.password = row[6]

        
        
        
        
        
        for row in reader:
            FriendsLisst = []
            f = F
            friends = row[4].split('|')
            i = 0;
            if (friends != None):
                for f in friends:
                    qualites = f.split(':') 
                    f = Friend(row[0], qualities[0], )
                    Friends[i].this = row[0]
                    Friends[i].friend = qualites[0]
                    Friends[i].contactTime = qualites[1]
                    i = i + 1
            p = ProVfile(row[0],row[1],row[2],Friends,row[4],row[5],row[6])
            profileList.append(p)

    return

class LoginScreen:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Wellness Check")
        self.topFrame = tk.Frame(self.window)

    def validateLogin(self,username, password):
        global profileList
        for p in profileList:
            if (username.get() == p.name and password.get() == p.password):
                print("matched!")
                return True
        print("wrong username or password");
        return

    def loginScreen(self):
        print("login screen")
        usernameLabel = tk.Label(self.window, text="User Name").grid(row=0, column=0)
        username = tk.StringVar()
        usernameEntry = tk.Entry(self.window, textvariable=username).grid(row=0, column=1)  
        passwordLabel = tk.Label(self.window,text="Password").grid(row=1, column=0)  
        password = tk.StringVar()
        passwordEntry = tk.Entry(self.window, textvariable=password, show='*').grid(row=1, column=1)  
        validatelogin = partial(self.validateLogin, username, password)
        loginButton = tk.Button(self.window, text="Login", command=validatelogin).grid(row=4, column=0)  

profileList=[]
readcsv()
printProfiles()
#row_count = sum(1 for row in fileObject)
gui = LoginScreen()
gui.loginScreen()
gui.window.mainloop()