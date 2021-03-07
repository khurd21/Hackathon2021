#!/usr/bin/python

import tkinter as tk
import csv
import json
import sys
from profile import Friend 
from profile import Profile
from functools import partial

def getLength():
    with open('data/users.csv','|', newline='') as f:
        return sum(1 for line in f)
def printProfiles():
    global profileList
    for p in profileList:
        print(p.name)
#Silas|10|None|1|{'Kyle':12,'Riley':15}|12345|hellamegaawesome|
#Kyle|3|None|0|None|1234|asdasdasdasd|
#Riley|10|None|0|None|123|pw|
#name, mood, avatar, contact, friendsList, id,password,
def readcsv():
    global profileList
    print("in read csv")
    with open('data/users.csv', newline='') as f:
        reader = csv.reader(f, delimiter='|')

        for row in reader:
            print(f"Name: {row[0]}")
            friend_list = []
            fr = Friend()
            p = Profile()
            p.name = row[0]
            p.mood = int(row[1])
            p.avatar = row[2]
            p.contact = int(row[3])
            #FRIENDS
            if row[4] == "None":
                js = None
            else: 
                #js = json.loads(row[4])
                js = eval(row[4])
                for j in js:
                    print(j)
                    fr.root = row[0]
                    fr.friend = j['Name']
                    fr.dateToContact = j['dateToContact']
                    fr.wellnessCheckFrequency = j['Name']
            p.id = row[5]
            p.password = row[6]
            profileList.append(p)
            #json.dump(p,sys.stdout)
    print("printing profile List")
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

def save_users():
    global profileList
    with open('data/users_test.csv', 'w') as f:
        #print("truncating")
        #f.truncate()
        for i in profileList:
            print("printing to outfile")
            i.save_user_data(f)
            #f.write("test")
    f.close()

profileList=[]
readcsv()
printProfiles()
save_users()
#print(profileList)
#profileList[0].save_user_data
#row_count = sum(1 for row in fileObject)
gui = LoginScreen()
gui.loginScreen()
gui.window.mainloop()