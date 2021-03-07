
#NOTES:
## for image stuff for Avatar: https://www.geeksforgeeks.org/working-images-python/


#   Need: Name, avatar, age  etc...
#
#
#
## IMPORTS:
#import emoji
#implement emoji using key value pair, valid emotions: happy, sad, exhausted, need help....
#emoji = {'happy':'U0001F603', 'sad:'U0001F603'} 
import sys
class Friend:
    def __init__ (self, root = "", dateToContact = "", friend = "",  wellnessCheckFrequency = 0):
        self.me = root
        self.dateToContact = dateToContact
        self.friend = friend
        self.wellnessCheckFrequency = wellnessCheckFrequency 

class Profile:
    def __init__(self, name = "", mood = "", avatar = "", contact = "1", friendsList = "", id = 0, password = ""):
        self.name = name
        self.mood = mood
        self.avatar = avatar
        self.contact = contact
        self.id = id;
        self.password = password
        self.friendsList = friendsList

    def save_user_data(self, f):
        f.write(f"{self.name}|{self.mood}|{self.avatar}|{self.contact}|[")
        jason = ""
        if self.friendsList != None:
            for fr in self.friendsList:
                jason += "{\"Name\":\""
                jason += fr.friend
                jason += "\",\"wellnessCheckFrequency\":\""
                jason += fr.wellnessCheckFrequency
                jason += "\",\"dateToContact\":\""
                jason += fr.dateToContact
                jason += "\"},"
                print(jason)
            jason = jason[:-1]
        else:
            jason += "None"
        f.write(jason)
        f.write(f"]|{self.id}|{self.password}|\n")

