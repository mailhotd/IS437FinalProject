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
        EventID = self.data[n]['EventID']
        UserID = self.data[n]['UserID']
        e = eventList()
        e.getById(EventID)
        EventName = e.data[0]['EventName']
        
        u = userList()
        u.getById(UserID)
        UserFName = u.data[0]['UserFName']
        
        now = datetime.now()
       
        prefix_text = UserFName + '\'s review of "' + EventName + '".  Reviwed on ' + str(now) + ' '
        
        if len(self.data[n]['review']) == 0:
            self.errorList.append("Review body cannot be blank.")
        else:
            self.data[n]['review'] = prefix_text + self.data[n]['review']

        if len(self.errorList) > 0:
            return False
        else:
            return True
            
    def getByUser(self,id):
    
        sql = '''SELECT * FROM `AttendanceTable` 
        LEFT JOIN `EventTable` ON `EventTable`.`EventID` = `AttendanceTable`.`EventID`
        WHERE  `AttendanceTable`.`UserID` = %s'''
        tokens = (id)
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        self.log(sql,tokens)
        cur.execute(sql,tokens)
        self.data = []
        for row in cur:
            self.data.append(row)