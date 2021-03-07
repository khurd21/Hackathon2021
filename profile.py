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
#Remove Friend class ?
class Friend:
    def __init__ (self, this = "", friend = "", contactTime = ""):
        self.me = this
        self.friend = friend
        self.contactTime = contactTime

class Profile:
    def __init__(self, name:str = "", mood:int = -1, avatar = "", contact:bool = False, id:str = ""):
        self.name:str = name
        self.mood:int = mood
        self.avatar:str = avatar
        self.contact:bool = contact
        self.id:str = id


