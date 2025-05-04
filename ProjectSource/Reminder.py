import datetime
import time
class Reminder:
    #Reminder
    #Date: Date python datetime format
    #Contents: A String just containing what the reminder is for
    def __init__(self,date,contents):
        self.date = date
        self.contents = contents
    def gettime(self):
        return self.date
    def getcontents(self):
        return self.contents
    def content(self,newcontent):
        self.contents = newcontent
    
