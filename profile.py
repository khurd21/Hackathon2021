
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

class Profile:
    def __init__(self, name = "", mood = "", avatar = "", contact = "1", friendsList = "", id = 0):
        self.name = name
        self.mood = mood
        self.avatar = avatar
        self.contact = contact
        self.id = id;

#class Friend:
#    def __init__ (self, this = "", friend = "", contactTime = ""):
#        self.me = this
#        self.friend = friend
#        self.contactTime = contactTime
##
##name, mood, avatar, contact, friendsList, id,password,
#class Profile:
#    def __init__(self, name = None, mood = None, avatar = None, contact = "1", friendsList = [], id = 0, password = ""):
#        self.name = name
#        self.mood = mood
#        self.avatar = avatar
#        self.contact = contact
#        self.id = id
#        self.password = password
#        self.friendsList = friendsList

########## utitlity functions ################
#    def printFriends(self):
#        i = 0
#        for f in friendsList:
#            print(f'Friend Name: {f.friend}\t#{i}\tcontactTime: {f.contactTime}')
            
######### ID ################
#    def id(self):
#        return self.id

#    #@property.setter
#    def set_id(self, id):
#        self.id =id

######### MOOD ################
#    def mood(self):
#        return self.mood

#    def set_mood(self, mood):
#        self.mood =mood 

######### NAME ################
#    def name(self):
#        return self.name

#    def set_name(self, name):
#        self.name = name

######### AVATAR ######
#    def get_avatar(self):
#        return self.avatar

#    def set_avatar(self, avatar):
#        self.avatar = avatar


