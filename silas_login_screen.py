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

def readcsv():
    global profileList
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
                    fr = Friend()
                    fr.root = row[0]
                    fr.friend = j['Name']
                    fr.dateToContact = j['dateToContact']
                    fr.wellnessCheckFrequency = j['Name']
                    friend_list.append(fr)
            p.friendsList = friend_list
            p.id = row[5]
            p.password = row[6]
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

    def deiconify(self):
        self.loginWindow.destroy()
        self.window.deiconify()


########### createProfile() not working, usr and pw are passign as blank strings ####################33
    def createProfile(self, widget, username, password, mood,contact):
        #print(username)
        #print(password)
        #   print(f"username: {username.get()} password: {password.get()} mood: {mood.get()} contact: {contact.get()}")
        #   global profileList
        #   p = Profile()
        #   p.name = username.get()
        #   p.password = password.get()
        #   #p.mood = int(float(mood.get()))
        #   #p.contact = int(contact.get())
        #   p.avatar = None
        #   p.friendsList = None
        #   profileList.append(p) 
        #   printProfiles()
        print("creating profile")

    def createProfileWindow(self):
        self.window.withdraw()
        self.loginWindow = tk.Tk()
        self.loginWindow.geometry("500x500")
        self.loginWindow.title("Wellness Check Login")
        self.loginTopFrame = tk.Frame(self.loginWindow)
        #data entry:
        usernameLabel = tk.Label(self.loginWindow, text="User Name").grid(row=0, column=0)
        username = tk.StringVar()
        usernameEntry = tk.Entry(self.loginWindow, textvariable=username).grid(row=0, column=1)  
        passwordLabel = tk.Label(self.loginWindow,text="Password").grid(row=1, column=0)  
        password = tk.StringVar()
        passwordEntry = tk.Entry(self.loginWindow, textvariable=password, show='*').grid(row=1, column=1)  
        
        moodLabel = tk.Label(self.loginWindow,text="Mood (1-10)").grid(row=2, column=0)  
        mood = tk.StringVar()
        moodEntry = tk.Entry(self.loginWindow, textvariable=mood).grid(row=2, column=1)  
        
        contactLabel = tk.Label(self.loginWindow,text="Do you want people to reach out? Y/N").grid(row=3, column=0)  
        contact = tk.StringVar()
        contactEntry = tk.Entry(self.loginWindow, textvariable=contact).grid(row=3, column=1)  
         
        #print(password.get())
        #buttons
        backToLogin = partial(self.deiconify)
        loginButton = tk.Button(self.loginWindow, text="Back To Login Window", command=backToLogin).grid(row=4, column=1)  

        createprofile = partial(self.createProfile,self.loginWindow, username, password, mood, contact)
        create_account = tk.Button(self.loginWindow, text="Create Account", command=createprofile).grid(row=4, column=0)  
        self.loginWindow.mainloop()
        #p = Profile()

    def loginScreen(self):
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

def save_users():
    global profileList
    with open('data/users_test.csv', 'w') as f:
        for i in profileList:
            print("printing to outfile")
            i.save_user_data(f)
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