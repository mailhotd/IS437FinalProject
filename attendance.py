import pymysql
from baseObject import baseObject
from user import userList
from event import eventList
from datetime import datetime
class attendanceList(baseObject):
    def __init__(self):
        self.setupObject('AttendanceTable')
        
    def verifyNew(self,n=0):
        self.errorList = []
        
        e = eventList()
        EventID = self.data[n]['EventID']
        e.getById(EventID)
        EventName = e.data[0]['EventName']
        
        u = userList()
        UserID = self.data[n]['UserID']
        u.getById(UserID)
        UserFName = u.data[0]['UserFName']
        UserLName = u.data[0]['UserLName']
        
        comment = UserFName + ' ' + UserLName + '\'s record for' + ' ' + EventName + '\n' + 'Comment: '
        
        if len(self.data[n]['UserEvaluation']) == 0:
            self.errorList.append("Evaluation body cannot be blank.")
        else:
            self.data[n]['UserEvaluation'] = comment + self.data[n]['UserEvaluation']

        if len(self.errorList) > 0:
            return False
        else:
            return True