
import tkinter as tk
from profile import Profile
from functools import partial


class CreateAccount:
    def __init__(self, profileList=[]):
        self.profileList = profileList
        self.window = tk.Tk()
        self.window.title("Wellness Check Account Creation")
        self.topFrame = tk.Frame(self.window)

    def destroyWindow(self):
        self.window.destroy()

########### createProfile() not working, usr and pw are passign as blank strings ####################33
    def createProfile(self, username, password, mood,contact):
        print(f"username: {username.get()} password: {password.get()} mood: {mood.get()} contact: {contact.get()}")
       # global profileList
        p = Profile()
        p.name = username.get()
        p.password = password.get()
        p.mood = int(mood.get())
        p.contact = int(contact.get())
        p.avatar = None
        p.friendsList = None
        self.profileList.append(p) 
        return 

    def printAccount(self, username, password):
        print("int printAccount")
        print(username.get())
        print(password.get())
        return 

#
    def displayScreen(self):
        usernameLabel = tk.Label(self.window, text="User Name").grid(row=0, column=0)
        username = tk.StringVar()
        usernameEntry = tk.Entry(self.window, textvariable=username).grid(row=0, column=1)  

        passwordLabel = tk.Label(self.window,text="Password").grid(row=1, column=0)  
        password = tk.StringVar()
        passwordEntry = tk.Entry(self.window, textvariable=password, show='*').grid(row=1, column=1)  

        moodLabel = tk.Label(self.window,text="Mood (1-10)").grid(row=2, column=0)  
        mood = tk.StringVar()
        moodEntry = tk.Entry(self.window, textvariable=mood).grid(row=2, column=1)  
        
        contactLabel = tk.Label(self.window,text="Do you want people to reach out? Y/N").grid(row=3, column=0)  
        contact = tk.StringVar()
        contactEntry = tk.Entry(self.window, textvariable=contact).grid(row=3, column=1)  
         
        createprofile = partial(self.createProfile, username, password, mood, contact)
        create_account = tk.Button(self.window, text="Create Account", command=createprofile).grid(row=4, column=0)  
        
        #printattr = partial(self.printAccount, username, password)
        #loginButton = tk.Button(self.window, text="print", command=printattr).grid(row=4, column=1)  

        gui.window.mainloop()

gui = CreateAccount()
gui.displayScreen()