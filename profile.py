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
class Friend:
    def __init__ (self, this = "", friend = "", contactTime = ""):
        self.me = this
        self.friend = friend
        self.contactTime = contactTime
#
#name, mood, avatar, contact, friendsList, id,password,
class Profile:
    def __init__(self, name = "", mood = "", avatar = "", contact = "1", friendsList = "", id = 0, password = ""):
        self.name = name
        self.mood = mood
        self.avatar = avatar
        self.contact = contact
        self.id = id
        self.password = password


######## ID ################
    #@property
    def id(self):
        return self.id

    #@property.setter
    def set_id(self, id):
        self.id =id
######## MOOD ################
    #@property
    def mood(self):
        return self.mood


    #@property.setter
    def set_mood(self, mood):
        self.mood =mood 
######## NAME ################
    #@property
    def name(self):
        return self.name

    #@property.setter
    def set_name(self, name):
        self.name = name
######## AVATAR ######
    #@property
    def get_avatar(self):
        return self.avatar

    #@property.setter
    def set_avatar(self, avatar):
        self.avatar = avatar


