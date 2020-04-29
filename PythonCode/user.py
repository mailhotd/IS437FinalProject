import pymysql
from baseObject import baseObject
class userList(baseObject):
    def __init__(self):
        self.setupObject('UserTable')
        
    def verifyNew(self,n=0):
        self.errorList = []
        
        u = userList()
        u.getByField('UserEmail',self.data[n]['UserEmail'])
        if len(u.data) > 0:
            self.errorList.append("Email address is already registered.")
        
        if len(self.data[n]['UserFName']) == 0:
            self.errorList.append("First name cannot be blank.")
        if len(self.data[n]['UserLName']) == 0:
            self.errorList.append("Last name cannot be blank.")
  
        if len(self.errorList) > 0:
            return False
        else:
            return True
            
    def verifyChange(self,n=0):
        self.errorList = []
        
        u = userList()
        u.getByField('UserEmail',self.data[n]['UserEmail'])
        #print(u.data)
        if len(u.data) > 0:
            print(self.data[n])
            print(u.data[0])
            if str(self.data[n]['id']) != str(u.data[0]['id']):
                self.errorList.append("Email address is already registered.")
        
        
        if len(self.data[n]['fname']) == 0:
            self.errorList.append("First name cannot be blank.")
        if len(self.data[n]['lname']) == 0:
            self.errorList.append("Last name cannot be blank.")
        
        if len(self.errorList) > 0:
            return False
        else:
            return True
            
    def tryLogin(self,email,pw):    
        #SELECT * FROM `UserTable` WHERE `email` = 'b@a.com' AND `password` = '123'
        sql = 'SELECT * FROM `' + self.tn + '` WHERE `UserEmail` = %s AND `UserPassword` = %s;'
        tokens = (email,pw)
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql,tokens)
        self.data = []
        n=0
        for row in cur:
            self.data.append(row)
            n+=1
        if n > 0:
            return True
        else:
            return False
    