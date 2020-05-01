import pymysql
from baseObject import baseObject
class eventList(baseObject):
    def __init__(self):
        self.setupObject('EventTable')
        
    def verifyNew(self,n=0):
        self.errorList = []
        
        if len(self.data[n]['EventName']) == 0:
            self.errorList.append("Event name cannot be blank.")
        if len(self.data[n]['EventStatus']) == 0:
            self.errorList.append("Event status cannot be blank.")
        if len(self.data[n]['EventSemester']) == 0:
            self.errorList.append("Event semester cannot be blank.")
        if len(self.data[n]['EventStartDT']) == 0:
            self.errorList.append("Event start cannot be blank.")
        if len(self.data[n]['EventEndDT']) == 0:
            self.errorList.append("Event end cannot be blank.")
  
        if len(self.errorList) > 0:
            return False
        else:
            return True
            
    def verifyChange(self,n=0):
        self.errorList = []
        
        if len(self.data[n]['EventName']) == 0:
            self.errorList.append("Event name cannot be blank.")
        if len(self.data[n]['EventStatus']) == 0:
            self.errorList.append("Event status cannot be blank.")
        if len(self.data[n]['EventSemester']) == 0:
            self.errorList.append("Event semester cannot be blank.")
        if len(self.data[n]['EventStartDT']) == 0:
            self.errorList.append("Event start cannot be blank.")
        if len(self.data[n]['EventEndDT']) == 0:
            self.errorList.append("Event end cannot be blank.")
            
        if len(self.errorList) > 0:
            return False
        else:
            return True