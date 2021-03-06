#NOTES:
## for image stuff for Avatar: https://www.geeksforgeeks.org/working-images-python/


#   Need: Name, avatar, age  etc...
#
#
#
## IMPORTS:
import emoji
#implement emoji using key value pair, valid emotions: happy, sad, exhausted, need help....
#emoji = {'happy':'U0001F603', 'sad:'U0001F603'} 
class Friend:
    def __init__ (self, this = "", friend = "", contactTime = ""):
        self.me = this
        self.friend = friend
        self.contactTime = contactTime

class Profile:
    def __init__(self, name = "", mood = "", avatar = "", contact = "1", friendsList = "", id = 0):
        self.name = name
        self.mood = mood
        self.avatar = avatar
        self.contact = contact
        self.id = id;


######## ID ################
    @property
    def id(self):
        return self.id

    @property.setter
    def set_name(self, id):
        self.id =id
######## MOOD ################
    @property
    def mood(self):
        return self.mood

    @property.setter
    def set_name(self, mood):
        self.mood =mood 
######## NAME ################
    @property
    def name(self):
        return self.name

    @property.setter
    def set_name(self, name):
        self.name = name
######## AVATAR ######
    @property
    def getAvatar(self):
        return self.avatar

    @property.setter
    def setAvatar(self, avatar):
        self.avatar = avatar


